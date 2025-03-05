import os
import pandas as pd
# Paths for audio files and text files
audio_folder = './wav'
tsv_folder = './text'

# def process_data():
# Load audio files
audio_files = {f for f in os.listdir(audio_folder) if f.endswith('.mp3') or f.endswith('.wav')}

# Dictionary to store text data
texts = {}

# Process TSV files
for tsv_file in os.listdir(tsv_folder):
    if tsv_file.endswith('.tsv'):
        tsv_path = os.path.join(tsv_folder, tsv_file)
        df_tsv = pd.read_csv(tsv_path, sep='\t', header=0)

        # Display number of columns and their names
        print(f"Processing {tsv_file}:")
        print(f"Number of columns: {df_tsv.shape[1]}")
        print(f"Columns: {df_tsv.columns.tolist()}")

        # Check if required columns exist
        if {'path', 'sentence'}.issubset(df_tsv.columns):
            for index, row in df_tsv.iterrows():
                audio_file_name = row['path']
                sentence_text = row['sentence']
                texts[audio_file_name] = sentence_text

        # Create a DataFrame from processed data
        df = pd.DataFrame(list(texts.items()), columns=['audio_file', 'text'])

        # Check if audio files exist
        df['audio_exists'] = df['audio_file'].apply(lambda x: x in audio_files)

        # Show missing audio files
        missing_audio = df[~df['audio_exists']]
        if not missing_audio.empty:
            print("Missing audio files:")
            print(missing_audio[['audio_file']])

        # Display total number of unique audio files and texts
        print(f"Total unique audio files: {df['audio_file'].nunique()}")
        print(f"Total texts: {df['text'].count()}")

        # Check if voting columns exist
        if {'up_votes', 'down_votes'}.issubset(df_tsv.columns):
            print("Up votes distribution:")
            print(df_tsv['up_votes'].describe())

            print("Down votes distribution:")
            print(df_tsv['down_votes'].describe())

            # Calculate total votes
            df_tsv['total_votes'] = df_tsv['up_votes'] + df_tsv['down_votes']
            print("Total votes distribution:")
            print(df_tsv['total_votes'].describe())

        # Analyze sentences
        if 'sentence' in df_tsv.columns:
            df_tsv['sentence_length'] = df_tsv['sentence'].apply(len)
            df_tsv['word_count'] = df_tsv['sentence'].apply(lambda x: len(x.split()))

            print("Sentence length distribution:")
            print(df_tsv['sentence_length'].describe())

            print("Word count distribution:")
            print(df_tsv['word_count'].describe())

            print("Sample sentences with their lengths and word counts:")
            print(df_tsv[['sentence', 'sentence_length', 'word_count']].head())

                                    # الگو برای شناسایی ترجمه نشده
            pattern = r'(?i)(N/A|None|ترجمه نشده)'  # به صورت غیر حساس به حروف بزرگ و کوچک

            # پیدا کردن خطوطی که شامل این الگو هستند
            untranslated_rows = df_tsv[df_tsv['sentence'].str.contains(pattern, na=False)]

            # نمایش نتایج
            print(f"untranslated_rows:{untranslated_rows}")
    # return df
