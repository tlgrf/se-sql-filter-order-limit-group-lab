import pandas as pd
import sqlite3

# ----------------------
# PART 1: Basic Filtering
# ----------------------

conn1 = sqlite3.connect('planets.db')

# planets with 0 moons
df_no_moons = pd.read_sql(
    "SELECT * FROM planets WHERE num_of_moons = 0;",
    conn1
)

# planets whose name is exactly 7 letters
df_name_seven = pd.read_sql(
    "SELECT name, mass FROM planets WHERE LENGTH(name) = 7;",
    conn1
)


# ----------------------
# PART 2: Advanced Filtering
# ----------------------

# mass ≤ 1.00
df_mass = pd.read_sql(
    "SELECT name, mass FROM planets WHERE mass <= 1.00;",
    conn1
)

# ≥1 moon AND mass < 1.00
df_mass_moon = pd.read_sql(
    "SELECT * FROM planets WHERE num_of_moons >= 1 AND mass < 1.00;",
    conn1
)

# color contains "blue"
df_blue = pd.read_sql(
    "SELECT name, color FROM planets WHERE color LIKE '%blue%';",
    conn1
)


# ----------------------
# PART 3: Ordering & Limiting
# ----------------------

conn2 = sqlite3.connect('dogs.db')

# hungry dogs sorted youngest→oldest
df_hungry = pd.read_sql(
    "SELECT name, age, breed FROM dogs WHERE hungry = 1 ORDER BY age ASC;",
    conn2
)

# hungry dogs age 2–7 sorted by name
df_hungry_ages = pd.read_sql(
    "SELECT name, age, hungry "
    "FROM dogs "
    "WHERE hungry = 1 AND age BETWEEN 2 AND 7 "
    "ORDER BY name ASC;",
    conn2
)

# the 4 oldest dogs (by age descending)
df_4_oldest = pd.read_sql(
    "SELECT name, age, breed FROM dogs ORDER BY age DESC LIMIT 4;",
    conn2
)


# ----------------------
# PART 4: Aggregation
# ----------------------

conn3 = sqlite3.connect('babe_ruth.db')

# total number of years played
df_ruth_years = pd.read_sql(
    "SELECT COUNT(*) AS total_years FROM babe_ruth_stats;",
    conn3
)

# total home runs
df_hr_total = pd.read_sql(
    "SELECT SUM(HR) AS total_home_runs FROM babe_ruth_stats;",
    conn3
)


# ----------------------
# PART 5: Grouping & Aggregation
# ----------------------

# for each team, number of years played
df_teams_years = pd.read_sql(
    "SELECT team AS team, COUNT(*) AS number_years "
    "FROM babe_ruth_stats "
    "GROUP BY team;",
    conn3
)

# for each team with avg at_bats > 200, average at-bats
df_at_bats = pd.read_sql(
    "SELECT team AS team, AVG(at_bats) AS average_at_bats "
    "FROM babe_ruth_stats "
    "GROUP BY team "
    "HAVING AVG(at_bats) > 200;",
    conn3
)


# ----------------------
# Close all connections
# ----------------------

conn1.close()
conn2.close()
conn3.close()