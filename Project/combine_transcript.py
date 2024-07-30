import pandas as pd

output_dir = "./output/"


def combine_transcript():
    li = []
    for i in range(1, 523):
        print(f"✔✔ {i}")
        df = pd.read_csv(
            f"{output_dir}/transcripts_{i}.csv",
            header=None,
            index_col=None,
            skiprows=1,
        )
        li.append(df)

    combined_df = pd.concat(li, axis=0, ignore_index=True)
    combined_df.to_csv(
        "combine_transcript_data.csv",
        index=None,
    )  # Exclude header from the output CSV


def combine_files(file1, file2):
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    
    df1['URL'] = df1['URL'].astype(str)  # Ensure URL column is of string type
    df2['id'] = df2['id'].astype(str)    # Ensure ID column is of string type

    combined_data = []
    
    for _, row1 in df1.iterrows():
        url = row1['URL']
        title = row1['Title']
        
        for _, row2 in df2.iterrows():
            id_str = row2['id']
            transcript = row2['transcript']
            
            if id_str in url:
                combined_data.append({
                    'URL': url,
                    'Title': title,
                    'Transcript': transcript
                })
                break  
    combined_df = pd.DataFrame(combined_data)
    
    combined_df.to_csv("combined_output.csv", index=False)
    print("Files combined and saved to 'combined_output.csv'")



def main():
    combine_files("combine_data.csv", "combine_transcript_data.csv")


if __name__ == "__main__":
    main()
