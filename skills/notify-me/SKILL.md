---
name: notify-me
description: Send a macOS notification when the user asks for a persistent, dismissible system alert, macOS alert, or osascript notification.
---

# macOS notifications

To send a Notification Center notification, run this command through `bash`:

```bash
message="..."
osascript -e 'on run argv' \
  -e 'display notification (item 1 of argv) with title "Pi"' \
  -e 'end run' \
  -- "$message"
```

Use the requested message as `message`. This sends a native macOS Notification Center notification without opening a window. For it to remain visible until dismissed, set the sending app's notification style to **Alerts** in System Settings → Notifications; **Banners** disappear automatically.
