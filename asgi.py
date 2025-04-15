from app import app

if __name__ == "__main__":  # 이 파이썬 파일을 명시적으로 실행했을때 if 아래 블록들이 실행된다.
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
