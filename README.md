## 📢 Django SSE Real-time Notification System

This project is a **real-time notification system using Server-Sent Events (SSE)** built with Django Rest Framework. It demonstrates how model changes (like creating a project, task, or comment) can trigger live browser notifications.

---

### 🎯 Objective

> Create an SSE in Django Rest Framework for a real-time notification system. Create two-three different models, any change in those should trigger a SSE to the client. Also maintain a notification model to store the change that triggered the notification and whether it was marked as read or not.

---

### 📦 Models

1. **Project** - Represents a project.
2. **Task** - Belongs to a project.
3. **Comment** - Belongs to a task.
4. **Notification** - Stores every triggered event and has `is_read` status.

---

### ✅ Features Implemented

- ✅ Model endpoints to **create Project, Task, Comment**
- ✅ SSE endpoint to **stream live notifications**
- ✅ Endpoint to **mark all notifications as read**
- ✅ **Ngrok live URL** to test externally
- ✅ Real-time frontend page to view updates


2. **Run the server**
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

3. **Start Ngrok**
```bash
ngrok http 8000
```
Copy the HTTPS URL shown by ngrok (used below).

---

### 🌐 Live NGROK URL

> 🔗 https://287f-2409-40f4-1022-d8b6-2037-d4f0-538c-8754.ngrok-free.app

---

### 🔗 API Endpoints

| Feature | Method | Endpoint | Description |
|--------|--------|----------|-------------|
| 🔨 Create Project | POST | `/api/projects/` | Creates a project |
| 📋 List Projects | GET | `/api/projects/` | Returns all projects |
| 🧩 Create Task | POST | `/api/tasks/` | Creates a task for a project |
| 📋 List Tasks | GET | `/api/tasks/` | Returns all tasks |
| 💬 Create Comment | POST | `/api/comments/` | Add comment to a task |
| 📋 List Comments | GET | `/api/comments/` | Returns all comments |
| 🔴 SSE Stream | GET | `/api/notifications/stream/` | Real-time notifications |
| ✅ Mark Read | POST | `/api/notifications/mark-read/` | Marks all notifications as read |

---

### 🖥️ Frontend UI

Open `index.html` or `test.html` in your browser:

```html
<!DOCTYPE html>
<html>
<head><title>Live Notifications</title></head>
<body>
  <h2>📢 Live Notifications</h2>
  <div id="stream"></div>
  <script>
    const evtSource = new EventSource("https://287f-2409-40f4-1022-d8b6-2037-d4f0-538c-8754.ngrok-free.app/api/notifications/stream/");
    evtSource.onmessage = function(e) {
      const div = document.getElementById("stream");
      const p = document.createElement("p");
      p.textContent = e.data;
      div.appendChild(p);
    };
  </script>
</body>
</html>
```

---

### 🔐 Assumptions

- SSE does not need user-level authentication (public stream).
- Client is expected to consume `/api/notifications/stream/` for updates.
- Only create operations are tracked for notification (not update/delete).
- Frontend connects via static HTML with `EventSource`.


https://287f-2409-40f4-1022-d8b6-2037-d4f0-538c-8754.ngrok-free.app/api/projects/


https://287f-2409-40f4-1022-d8b6-2037-d4f0-538c-8754.ngrok-free.app/api/tasks/


https://287f-2409-40f4-1022-d8b6-2037-d4f0-538c-8754.ngrok-free.app/api/comments/

https://287f-2409-40f4-1022-d8b6-2037-d4f0-538c-8754.ngrok-free.app/api/notifications/stream/
