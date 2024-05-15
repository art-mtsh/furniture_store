import os


def rename_files(directory):
    # Iterate through files in the directory
    for filename in os.listdir(directory):
        # Split the filename into words
        words = filename.split('.')

        m_type = words[0]
        m_manu = words[1]
        m_title = words[2]
        m_color = words[2]

        print(f'Тип: {m_type}, виробник: {m_manu}, назва: {m_title}, колір: {m_color}')

        # # Check if there are at least three words in the filename
        # if len(words) >= 3:
        #     # Extract the first two words
        #     material = words[0]
        #     brand = words[1]
        #
        #     # Join the remaining words as the name
        #     name = ' '.join(words[2:])
        #
        #     # Construct the new filename
        #     new_filename = f"{material}.{brand}.{name}"

            # Rename the file
            # os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            # print(f"Renamed '{filename}' to '{new_filename}'")


# Provide the directory path
directory_path = "D:\IT\Pycharm Projects\MyStore CREDENTIALS\МАТЕРІАЛИ\Тканини"

# Call the function to rename files in the directory
rename_files(directory_path)