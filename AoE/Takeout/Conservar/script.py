import os
import json
import re

def process_json_files():
    print("Starting to process JSON files...")
    base_folder = r"C:\Users\Portatil\Desktop\Obsidian Projects\AoE\Takeout\Conservar"
    # Create output folders if they don't exist
    for folder in ['Advent_of_Ether', 'AOE_Lore', 'Other']:
        os.makedirs(os.path.join(base_folder, folder), exist_ok=True)
    print("Output folders created.")

    # Scan all JSON files in the base directory
    json_files = [f for f in os.listdir(base_folder) if f.endswith('.json')]
    print(f"Found {len(json_files)} JSON files to process.")
    for filename in json_files:
        print(f"Processing file: {filename}")
        try:
            with open(os.path.join(base_folder, filename), 'r', encoding='utf-8') as file:
                data = json.load(file)
            
            # Extract labels
            labels = data.get('labels', [])
            
            # Extract required information
            title = os.path.splitext(filename)[0]
            text_content = data.get('textContent', '')
            
            # Process attachments
            file_path = ''
            attachments = data.get('attachments', [])
            if attachments:
                for attachment in attachments:
                    file_path = attachment.get('filePath', '')
                    if file_path:
                        src_path = os.path.join(base_folder, file_path)
                        if os.path.exists(src_path):
                            file_path = os.path.basename(file_path)
                        else:
                            print(f"Warning: Image file not found: {src_path}")
                            file_path = ''
                        break  # Only process the first valid attachment
            
            # Create markdown content
            markdown_content = f"{text_content}"
            if file_path:
                markdown_content = f"![{title}]({file_path})\n\n{markdown_content}"
            
            # Copy file to each label's folder
            for label in labels:
                label_name = label.get('name')
                if label_name:
                    output_folder = os.path.join(base_folder, label_name)
                    os.makedirs(output_folder, exist_ok=True)
                    
                    output_file = os.path.join(output_folder, f"{title}.md")
                    with open(output_file, 'w', encoding='utf-8') as out_file:
                        out_file.write(markdown_content)
                    
                    print(f"Copied to: {output_file}")
                    
                    # Copy image if it exists
                    if file_path:
                        src_path = os.path.join(base_folder, file_path)
                        dst_path = os.path.join(output_folder, file_path)
                        if os.path.exists(src_path):
                            import shutil
                            shutil.copy2(src_path, dst_path)
                            print(f"Copied image: {src_path} -> {dst_path}")
            
            # If no labels, copy to 'Other' folder
            if not labels:
                output_folder = os.path.join(base_folder, 'Other')
                output_file = os.path.join(output_folder, f"{title}.md")
                with open(output_file, 'w', encoding='utf-8') as out_file:
                    out_file.write(markdown_content)
                print(f"Copied to: {output_file}")
                
                # Copy image to 'Other' folder if it exists
                if file_path:
                    src_path = os.path.join(base_folder, file_path)
                    dst_path = os.path.join(output_folder, file_path)
                    if os.path.exists(src_path):
                        import shutil
                        shutil.copy2(src_path, dst_path)
                        print(f"Copied image: {src_path} -> {dst_path}")
            
            print(f"Processed: {filename}")
        except json.JSONDecodeError:
            print(f"Error: {filename} is not a valid JSON file.")

    print("Finished processing all JSON files.")

if __name__ == "__main__":
    process_json_files()
