import django.contrib.sessions.backends.db as db

class SessionStore(db.SessionStore):
    sessions = 0

    def _get_new_session_key(self):
        while True:
            session_key = 'JuhosSessions-' + str(SessionStore.sessions)
            SessionStore.sessions += 1
            if not self.exists(session_key):
                return session_key
