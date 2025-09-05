from generic_code import code_library
from schema import src_stg_schema
import json

### Read from config file.
config_snow_copy = open('./config/copy_to_snowstg_avro_v1.json', "r")
config_snow_copy = json.loads(config_snow_copy.read())

connection_parameter = open('./config/connection_details.json', "r")
connection_parameter = json.loads(connection_parameter.read())


session = code_library.snowconnection(connection_parameter)
copied_into_result, qid = code_library.copy_to_table_semi_struct_data(session,config_snow_copy,src_stg_schema.emp_details_avro_cls)


print(copied_into_result)
print(qid)

copied_into_result_df = session.create_dataframe(copied_into_result)
copied_into_result_df.show()