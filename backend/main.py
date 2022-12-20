import uuid
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from postgres import PostgresConnection
from create_tables import create_tables

create_tables()

class User(BaseModel):
    u_name: str
    u_email: str
    u_password: str

app = FastAPI()

@app.post("/users/register")
def register(user: User):
    print(user)
    with PostgresConnection() as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO users (u_id, u_name, u_email, u_password) values ('{}', '{}', '{}', '{}')".format(
           str(uuid.uuid4()), user.u_name, user.u_email, user.u_password
        ))
        conn.commit()
        return {"status": "success", "message": "User registered successfully"}

if __name__ == "__main__":
    create_tables()
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")