import sqlglot
import streamlit as st
from streamlit_ace import st_ace

app_name = "SQL Translator"
dialects = (
    "athena",
    "bigquery",
    "clickhouse",
    "databricks",
    "doris",
    "drill",
    "druid",
    "duckdb",
    "hive",
    "materialize",
    "mysql",
    "oracle",
    "postgres",
    "presto",
    "prql",
    "redshift",
    "risingwave",
    "snowflake",
    "spark",
    "spark2",
    "sqlite",
    "starrocks",
    "tableau",
    "teradata",
    "trino",
    "tsql",
)

st.set_page_config(page_title=app_name, layout="wide")

st.title(app_name)
st.write(f"Translate SQL queries between {len(dialects)} different dialects")
st.markdown(
    "[![Built by North Star](https://img.shields.io/badge/built_by-North_Star_Data-4F46E5)](https://northstardata.co/)"
)
st.divider()

col1, col2 = st.columns(2)

with col1:
    input_dialect = st.selectbox(label="Input", options=dialects, index=7)
    input_query = st_ace(
        value="SELECT EPOCH_MS(1618088028295)",
        placeholder="Write your SQL query here",
        language="sql",
        theme="dracula",
    )

with col2:
    output_dialect = st.selectbox(label="Output", options=dialects, index=8)
    output_query = sqlglot.transpile(
        sql=input_query, read=input_dialect, write=output_dialect, pretty=True
    )[0]
    output = st_ace(
        value=output_query,
        language="sql",
        theme="dracula",
        readonly=True,
        auto_update=True,
    )
