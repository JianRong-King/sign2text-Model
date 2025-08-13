import os
import json
import pickle
import numpy as np
from tqdm import tqdm
from concurrent.futures import ProcessPoolExecutor
#Replace file paths and include the imports above
def process_json_file(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)

    pose_data = []
    for person in data.get('people', []):
        # Extract keypoints in the specified order
        for key in ['pose_keypoints_2d', 'hand_left_keypoints_2d', 'hand_right_keypoints_2d', 'face_keypoints_2d']:
            if key in person:
                pose_data.extend(person[key])

    # Reshape to (vertices, channels)
    pose_array = np.array(pose_data).reshape(-1, 3)
    return pose_array

def process_subfolder(subfolder_path, output_folder):
    json_files = sorted([f for f in os.listdir(subfolder_path) if f.endswith('.json')])
    frame_data = []

    for json_file in tqdm(json_files, desc=f"Processing {subfolder_path}"):
        json_path = os.path.join(subfolder_path, json_file)
        frame_data.append(process_json_file(json_path))

    # Stack frames along the time axis: (Time, Vertices, Channels)
    frame_data = np.stack(frame_data)

    # Save to .pkl
    output_path = os.path.join(output_folder, os.path.basename(subfolder_path) + '.pkl')
    with open(output_path, 'wb') as f:
        pickle.dump(frame_data, f)

def main(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    subfolders = [os.path.join(input_folder, d) for d in os.listdir(input_folder) if os.path.isdir(os.path.join(input_folder, d))]

    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(process_subfolder, subfolder, output_folder) for subfolder in subfolders]
        for future in tqdm(futures, desc="Overall Progress"):
            future.result()

if __name__ == "__main__":

    
    input_folder = "how2sign\dataset\openpose_output\json"
    output_folder = "how2sign\dataset\openpose_output\pkl"
    main(input_folder, output_folder)


    # C:\Monash\Y3_SEM-2\FYP_2\Alt\Glofe\GloFE-main\json_to_pkl.py