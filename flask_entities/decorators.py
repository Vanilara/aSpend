from flask import request, session, redirect
from functools import wraps
from config import Config


class ParamsHandler:
    @staticmethod
    def take_form_params(params):
        def decorator(func):
            @wraps(func)
            def decorated_function(*args, **kwargs):
                for param in params:
                    kwargs[param] = request.form.get(param)
                return func(*args, **kwargs)
            return decorated_function
        return decorator
    
class SessionHandler:
    @staticmethod
    def take_alerts(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            kwargs['alerts'] = session.pop('alerts', None)
            return f(*args, **kwargs)
        return decorated_function
    
    @staticmethod
    def take_user_id(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if Config.IS_DEBUG:
                kwargs['user_id'] = 1
            else:
                if not session.get('user_id'):
                    return redirect('/login')
                kwargs['user_id'] = session.get('user_id')
            return f(*args, **kwargs)
        return decorated_function