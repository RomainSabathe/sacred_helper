import os
import pytest

from sacred_helper import PastExperiment


def test_get_metric():
    url = os.environ('SERVER_IP')
    uri = f'{url}:27017'
    experiment_id = 1
    database_name = 'oulu_protocol_4'

    experiment = PastExperiment(uri=uri, experiment_id=experiment_id,
                                database_name=database_name)

    metric = experiment.get_metric('val_accuracy')

    with pytest.raises(AttributeError):
        experiment.get_metric('test_accuracy')


def test_get_config():
    url = os.environ('SERVER_IP')
    uri = f'{url}:27017'
    experiment_id = 1
    database_name = 'oulu_protocol_4'

    experiment = PastExperiment(uri=uri, experiment_id=experiment_id,
                                database_name=database_name)

    config = experiment.get_config()
    assert 'dataset_config' in config
