"""
L10 — Data Explorer  (STARTER)
================================
Run with:
    streamlit run starter.py

Your goal: build a Streamlit app that fetches and explores user data
from JSONPlaceholder.

Required features:
    1. Fetch users from https://jsonplaceholder.typicode.com/users
       using @st.cache_data(ttl=300)
    2. Display 3 metrics: total users, most common city, avg latitude
    3. Sidebar text_input to filter users by name
    4. st.dataframe() showing the filtered users
    5. st.bar_chart() showing users per city

Key concepts:
    @st.cache_data(ttl=300)
        → Caches the function's return value.
        → Re-runs only when inputs change or after 300 seconds.
        → Without it, the API is called on EVERY widget interaction.

    st.dataframe()  — interactive, sortable table
    st.table()      — static, non-interactive table (better for small data)

    st.metric(label, value, delta, delta_color)
        delta_color:
            "normal"  — green if positive, red if negative (default)
            "inverse" — red if positive, green if negative
            "off"     — neutral grey regardless of sign
"""

import streamlit as st
import requests

# ── Step 1: Page config ────────────────────────────────────────────────────
# TODO: st.set_page_config with layout="wide", title, and icon

# ── Step 2: Cached data fetch ──────────────────────────────────────────────
# TODO: Define fetch_users() decorated with @st.cache_data(ttl=300)
# Inside: GET https://jsonplaceholder.typicode.com/users
#         response.raise_for_status() — raises for 4xx/5xx
#         return response.json()
#
# User object shape:
# {
#   "id": 1, "name": "Leanne Graham", "email": "...",
#   "address": {"city": "Gwenborough", ...},
#   "geo": {"lat": "-37.3159", "lng": "81.1496"},
#   "company": {"name": "Romaguera-Crona"},
#   ...
# }


# ── Step 3: Load data ──────────────────────────────────────────────────────
# TODO: Call fetch_users() inside a st.spinner() context manager
# users = fetch_users()

# ── Step 4: Derived metrics ────────────────────────────────────────────────
# TODO: Calculate:
#   total_users      = len(users)
#   city_counts      = dict counting how many users per city
#   most_common_city = city with the highest count
#   avg_lat          = average of float(user["geo"]["lat"]) for all users
# Hint for city_counts: use a loop + dict.get(key, 0) + 1

# ── Step 5: Page title ────────────────────────────────────────────────────
# TODO: st.title and st.caption

# ── Step 6: Metrics row ───────────────────────────────────────────────────
# TODO: Create 3 columns and display a st.metric() in each
# col1, col2, col3 = st.columns(3)
#
# with col1: st.metric("👥 Total Users", total_users)
# with col2: st.metric("🏙️ Most Common City", most_common_city, ...)
# with col3: st.metric("🌍 Avg. Latitude", f"{avg_lat:.2f}°", ...)
# Use delta_color="off" for the city metric to avoid misleading colour coding

# ── Step 7: Sidebar filter ────────────────────────────────────────────────
# TODO: with st.sidebar: add a text_input to filter users by name
# Store the value in name_filter

# TODO: Filter users:
#   if name_filter: filtered_users = [u for u in users if ...]
#   else: filtered_users = users

# ── Step 8: Data table ────────────────────────────────────────────────────
# TODO: Build a list of flat dicts for display (name, email, city, company)
# TODO: st.dataframe(table_rows, use_container_width=True, hide_index=True)

# ── Step 9: Bar chart ─────────────────────────────────────────────────────
# TODO: st.subheader and st.bar_chart(city_counts)
