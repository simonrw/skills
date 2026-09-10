---
name: notify-me
description: Send a push notification through ntfy.sh when the user asks to be notified or alerted, including when a task finishes.
---

# ntfy notifications

Use the user's requested topic, or `NTFY_TOPIC` from the environment. If neither is available, ask for the topic before sending. Topic names must be 1-64 characters using only letters, numbers, underscores, and hyphens. The user must subscribe to that topic on ntfy.sh in the ntfy app or web app to receive notifications.

Unprotected topics are public to anyone who knows the name. Recommend a hard-to-guess topic and keep secrets and sensitive details out of messages.

Set `message` to the requested text, or a brief task result when notifying on completion. Quote it as literal shell data. Run through `bash`, setting `NTFY_TOPIC` locally if the user supplied it:

```bash
message='...'
printf '%s' "$message" | curl --fail --silent --show-error --max-time 30 \
  -H 'Title: Pi' \
  --data-binary @- \
  "https://ntfy.sh/${NTFY_TOPIC:?Set NTFY_TOPIC to your subscribed topic}"
```

Report success only when the request succeeds. This confirms publication, not delivery to a device. On failure, report the error rather than falling back to a macOS notification.

Reference: [ntfy publishing documentation](https://docs.ntfy.sh/publish/).
