import sys
import os
from django.apps import AppConfig

class PredictorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'predictor'

    def ready(self):
        # Preload the TabPFN model at startup so inference is instantaneous
        if os.environ.get('RUN_MAIN') == 'true' or 'test' in sys.argv or 'runserver' not in sys.argv:
            try:
                from .ml_service import MLService
                MLService.get_instance()
            except Exception as e:
                print(f"[PredictorConfig] Notice: MLService preload deferred: {e}")
