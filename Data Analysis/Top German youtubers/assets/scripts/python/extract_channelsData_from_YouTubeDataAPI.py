import pandas as pd
from googleapiclient.discovery import build

# Replace with your YouTube API key
API_KEY = 'AIzaSyD8LrILty0o_R9KXsHcqpHFU8WzH6pXdTA'

# Build the YouTube service object
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Load the CSV file containing YouTube Channel Names and IDs
file_path = '../dataset/youtube_data_germany.csv'  # Path to your uploaded CSV file
df = pd.read_csv(file_path)

# Function to fetch YouTube channel statistics
def get_channel_stats(channel_id):
    try:
        request = youtube.channels().list(
            part="statistics",
            id=channel_id
        )
        response = request.execute()
        
        if 'items' in response and response['items']:
            stats = response['items'][0]['statistics']
            return {
                'subscribers': stats.get('subscriberCount', 'N/A'),
                'total_views': stats.get('viewCount', 'N/A'),
                'total_videos': stats.get('videoCount', 'N/A'),
                'channel_id': channel_id
            }
        else:
            print(f"No data found for Channel ID: {channel_id}")
            return {
                'subscribers': 'N/A',
                'total_views': 'N/A',
                'total_videos': 'N/A',
                'channel_id': channel_id
            }
    except Exception as e:
        print(f"Error fetching data for Channel ID: {channel_id} - {e}")
        return {
            'subscribers': 'N/A',
            'total_views': 'N/A',
            'total_videos': 'N/A',
            'channel_id': channel_id
        }

# Extract channel IDs by splitting the "NAME" column at '@'
df['Channel_Id'] = df['NAME'].str.split('@').str[1].str.strip()

# List to store channel statistics dictionaries
channel_stats = []

# Iterate through the DataFrame and get channel stats for each ID
for channel_id in df['Channel_Id']:
    stats = get_channel_stats(channel_id)
    channel_stats.append(stats)

# Convert the list of stats to a DataFrame
stats_df = pd.DataFrame(channel_stats)

# Reset index to align both dataframes
df.reset_index(drop=True, inplace=True)
stats_df.reset_index(drop=True, inplace=True)

# Concatenate the dataframes horizontally
combined_df = pd.concat([df, stats_df], axis=1)

# Adding the channel name to the dataframe
combined_df['Channel_name'] = df['NAME'].str.split('@').str[0]

# Optionally, drop the 'channel_name' column from stats_df if needed (commented out here)
# combined_df.drop('channel_name', axis=1, inplace=True)

# Save the merged dataframe back into a CSV file
output_file = '../dataset/updated_youtube_data_germany.csv'
combined_df.to_csv(output_file, index=False)

# Show the first 10 rows
print(combined_df.head(10))
