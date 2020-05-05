import numpy as np


class TreeEnsemble:
    def __init__(self, x, y, n_trees, sample_size, min_leaf=5):
        np.random.seed(55)
        self.x = x
        self.y = y
        self.sample_size = sample_size
        self.min_leaf = min_leaf
        self.trees = [self.create_tree() for i in range(n_trees)]

    def create_tree(self):
        idxs = np.random.permutation(len(self.y))[: self.sample_size]
        return DescisionTree(
            self.x.iloc[idxs],
            self.y[idxs],
            idxs=np.array(range(self.sample_size)),
            min_leaf=self.min_leaf,
        )

    def predict(x):
        return np.mean([t.predict(x) for t in self.trees], axis=0)


class DescisionTree:
    def __init__():
        return


if __name__ == "__main__":
    idxs = np.random.permutation(25)[:5]
    print(idxs)