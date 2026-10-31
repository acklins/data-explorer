import streamlit as st
import requests
import pandas as pd

# ── Page config ────────────────────
st.set_page_config(
    page_title="User Data Explorer",
    page_icon="📊",
    layout="wide"
)
# ── Cached data fetch ──────────
@st.cache_data(ttl=300)
def fetch_users():

    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url, timeout=10)

    response.raise_for_status()

    return response.json()


# ── Load data ─────────────
try:
    with st.spinner("Loading user data..."):
        users = fetch_users()

except requests.exceptions.RequestException as e:
    st.error(f"Unable to fetch users: {e}")
    st.stop()

# ── Derived metrics ─────────
total_users = len(users)

#Users per city
city_counts = {}

for user in users:

    city = user["address"]["city"]

#Returns the current count/ 0 if no city
    city_counts[city] = city_counts.get(city, 0) + 1

#Retrieves the city with the highest count
if city_counts:
    most_common_city = max(city_counts, key=city_counts.get)
else:
    most_common_city = "N/A"

#Average latitude; nested json structure
if users:
    total_lat = sum(
        float(user["address"]["geo"]["lat"])
        for user in users
    )
    avg_lat = total_lat / total_users
else:
    avg_lat = 0

# ── Page title ──────────────
st.title("📊 User Data Explorer")

st.caption(
    "Explore user information retrieved from JSONPlaceholder API."
)

st.divider()

# ──Metrics row ────────
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="👥 Total Users",
        value=total_users
    )

with col2:
    st.metric(
        label="🏙️ Most Common City",
        value=most_common_city
    )

with col3:
    st.metric(
        label="🌍 Average Latitude",
        value=f"{avg_lat:.2f}°"
    )
# ── Sidebar filter ───────
with st.sidebar:

    st.header("Filters")

    name_filter = st.text_input(
        "Search users by name",
        placeholder="Enter a name..."
    )

if name_filter:

#expression checks each users name
    filtered_users = [
        user for user in users
        if name_filter.lower() in user["name"].lower()
    ]

else:
    filtered_users = users

# ── Interactive DataFrame──────────
st.subheader("User Directory")

table_rows = []

for user in filtered_users:

    table_rows.append({
        "Name": user["name"],
        "Email": user["email"],
        "City": user["address"]["city"],
        "Company": user["company"]["name"]
    })

df = pd.DataFrame(
    table_rows,
    columns=["Name", "Email", "City", "Company"]
)

st.write(f"Showing {len(filtered_users)} of {total_users} users")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

# ── Bar chart ───────────
st.subheader("Users per City")

city_df = pd.DataFrame(
    list(city_counts.items()),
    columns=["City", "Users"]
)

city_df = city_df.set_index("City")

st.bar_chart(city_df)
