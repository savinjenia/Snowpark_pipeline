from generic_code import code_library

# Make connection and create Snowpark session.
# Please mention your snowflake account credentials below,
connection_parameters = {"account":"EFPKHYG-KT18285",
                         "user":"ISAVIN",
                         "password": "8ZRu7mhptF2Q37D",
                         "role":"ACCOUNTADMIN",
                         "warehouse":"COMPUTE_WH",
                         "database":"DEMO_DB",
                         "schema":"PUBLIC"
}

# Create connection with snowflake and return the session
session = code_library.snowconnection(connection_parameters)