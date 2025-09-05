# This file belongs to lecture,
# https://www.udemy.com/course/snowpark-data-engineering-with-snowflake/learn/lecture/36040084#overview
from generic_code import code_library
from schema import src_stg_schema
import json

### Read from config file.
config_snow_copy = open('./config/copy_to_snowstg_avro.json', "r")
config_snow_copy = json.loads(config_snow_copy.read())

connection_parameter = open('./config/connection_details.json', "r")
connection_parameter = json.loads(connection_parameter.read())

session = code_library.snowconnection(connection_parameter)

df = session.read.avro("@my_s3_stage/Avro_folder/userdata1.avro")

copied_into_result, qid = code_library.copy_to_table_semi_struct_data(session,config_snow_copy,src_stg_schema.int_emp_details_avro)


print(copied_into_result)
print(qid)

copied_into_result_df = session.create_dataframe(copied_into_result)
copied_into_result_df.show()
