import re
import os


def create_proto():

    proto = open("schedule1.proto", "w", encoding="UTF-8")
    res = """syntax="proto2";

message day {
 required string day = 1;   
 required Parity parity = 2; 
}
message Parity{
    required string parity = 1;
    required Pair pair = 2;
}
message Pair{
 required string time = 1;
 required string aud = 2;
 required string place = 3;
 required string thing = 4;
 required string teacher = 5;
}"""

    proto.write(res)
    proto.close()


def convert_from_json_to_proto(json_filename):
    create_dict(json_filename)
    from dict import dict

    import Schedule1_pb2

    days = []
    for key in dict:
        day = Schedule1_pb2.Day()
        day.name = key
        for inner_key in dict[key]:

            day.parity = inner_key + " "
            for inner_dict in dict[key][inner_key]:
                day.pair += "\n"
                for inner_dict_key in inner_dict:
                    day.pair += inner_dict_key + ": "
                    day.pair += inner_dict[inner_dict_key] + "\n"
                day.pair += "\n"
        days.append(day)

    for i in days:

        print(i.name, i.parity +"\n", i.pair, end="---------\n")


def create_dict(json_filename):
    f = open(json_filename, "r", encoding="UTF-8")
    data = f.read()
    f.close()
    data = re.sub("\n", "", data)

    python_file = open("dict.py", "w", encoding="UTF-8")
    res = "dict =" + data
    python_file.write(res)
    python_file.close()


convert_from_json_to_proto("schedule.json")

"""protoc -I=$SRC_DIR --python_out=$DST_DIR $SRC_DIR/addressbook.proto"""
