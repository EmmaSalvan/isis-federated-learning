import matplotlib.pyplot as plt
import seaborn as sns

digits = list(range(0, 10))


def plot_distribution(client_datasets):
    fig, ax = plt.subplots(1, 3, figsize=(20, 7))
    axs = [a for a in ax]

    nb_data = 0
    for i, client_data in enumerate(client_datasets):
        labels = [data[1] for data in client_data]
        labels.append(-1)
        nb_data += len(labels)
        ax_ = sns.histplot(labels, binwidth=0.4, ax=axs[i], bins=digits)
        ax_.set_xlim(-0.5, 10)
        ax_.set_xticks(range(0, 10))

    plt.show()


def plot_example_images(train_data):
    fig = plt.figure()
    for i in range(3):
        plt.subplot(1, 3, i + 1)
        plt.tight_layout()
        image, label = train_data[i]
        plt.imshow(image.squeeze(), cmap=plt.get_cmap("gray"))
        plt.title("Ground Truth: {}".format(label))
        plt.xticks([])
        plt.yticks([])
    plt.show()
