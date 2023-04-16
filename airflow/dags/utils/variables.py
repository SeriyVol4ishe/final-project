from airflow.models import Variable


class VariablesGetter:
    def __init__(self, namespace: str, keys: list[str]):
        self.namespace = namespace
        self.keys = keys
        self.data = None

    def __getitem__(self, key):
        if key not in self.keys:
            raise KeyError('Key is not presented in keys list.')
        if self.data is None:
            self.data = Variable.get(
                self.namespace,
                deserialize_json=True,
            )
        return self.data[key]
