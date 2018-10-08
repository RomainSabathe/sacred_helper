from sacredboard.app.data.pymongo.mongodb import PyMongoDataAccess


class PastExperiment(object):
    def __init__(self, database_name, experiment_id, uri=None):
        self.database_name = database_name
        self.experiment_id = experiment_id
        self.uri = uri
        self.collection_name = 'runs'

        self.generic_dao = PyMongoDataAccess(
            uri=self.uri,
            database_name=self.database_name,
            collection_name=self.collection_name)
        self.generic_dao.connect()

        self.metrics_dao = self.generic_dao.get_metrics_dao()
        self.run_dao = self.generic_dao.get_run_dao()

        self.run = self.run_dao.get(experiment_id)
        self.info = self.run.get('info')
        self.metrics_info = self.info.get('metrics')

    def get_metric(self, metric_name):
        metric_id = None
        # self.metrics_info is a list of dicts
        for metric_info in self.metrics_info:
            if metric_info.get('name') == metric_name:
                metric_id = metric_info.get('id')
                break
        else:
            raise AttributeError(f"Can't find metric {metric_name}")

        metric = self.metrics_dao.get(self.experiment_id, metric_id)
        return metric

    def get_config(self):
        return self.run['config']
