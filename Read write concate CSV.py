import os
import pandas as pd
final_df = pd.DataFrame()

with open("D:\Python\paymentDTO\InitiatePaymentDTO.txt", "r") as original_file:
    for line in original_file:
        if "InitiatePaymentDTO" in line:
            start_index = line.index("(") + 1
            end_index = line.index(")")
            content = line[start_index:end_index]
            data_dict = {}
            content_sublist = content.split(",")
            for item in content_sublist:
                key, value = item.split("=")
                key = key.strip()
                value = value.strip()
                if key in data_dict:
                    data_dict[key].append(value)
                else:
                    data_dict[key] = [value]
            df = pd.DataFrame(data_dict)
            final_df = final_df._append(df, ignore_index=True)
                


final_df.to_csv("InitiatePaymentDTO.csv", mode='a', header=not os.path.exists("InitiatePaymentDTO.csv"), index=False)
