from io import BytesIO
import base64
import matplotlib.pyplot as plt
import seaborn as sns

def plot(x , y , labelx , labely , titre, df ):
    img = BytesIO()

    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(figsize = (8,5))
    plt.title(titre, fontdict={'fontweight': 600,'fontsize':13},y=1)
    plt.xticks(fontweight = 600)
    plt.yticks(fontweight = 600)
    sns.barplot(x = '_id', y = y, data = df , ax = ax)
    plt.xlabel(labelx, fontsize=13, x=0.5)
    plt.ylabel(labely, fontsize=13)

    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)

    return base64.b64encode(img.getvalue())

