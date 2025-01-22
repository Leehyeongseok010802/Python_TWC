import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import time
import random

def execute_notebook(notebook_path):
    with open(notebook_path) as f:
        notebook = nbformat.read(f, as_version=4)
    
    execute_preprocessor = ExecutePreprocessor(timeout=600, kernel_name='python3')
    execute_preprocessor.preprocess(notebook, {'metadata': {'path': './'}})

def main():
    crowling_folder = "./Crowling_py"
    if os.path.exists(crowling_folder):
        for notebook in os.listdir(crowling_folder):
            if notebook.endswith(".ipynb"):
                notebook_path = os.path.join(crowling_folder, notebook)
                print(f"Running {notebook_path}...")
                try:
                    execute_notebook(notebook_path)
                    print(f"{notebook_path} 실행 완료!")
                except Exception as e:
                    print(f"Error running {notebook_path}: {e}")
                sleep_time = random.uniform(5, 10)  # 5초에서 10초 사이의 랜덤 대기
                print(f"Waiting for {sleep_time:.2f} seconds before next notebook...")
                time.sleep(sleep_time)
    else:
        print(f"{crowling_folder} 경로를 찾을 수 없습니다.")

if __name__ == "__main__":
    main()
