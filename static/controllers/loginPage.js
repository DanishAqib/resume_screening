const data = {
  u_name: "test",
  u_email: "test@gmail.com",
  u_password: "test",
};

document.getElementById("signup-btn").addEventListener("click", async () => {
  fetch("http://localhost:8000/users/register", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
  .then(response => response.json())
  .then(result => console.log(result))
  .catch(error => console.error(error));
});