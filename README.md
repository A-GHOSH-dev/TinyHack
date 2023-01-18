# TinyHack

[embed]https://github.com/A-GHOSH-dev/TinyHack/blob/master/lifeai.pdf[/embed]

Multiple Disease detection Software in Django Python.

Alzheimer's disease Detection from fMRI Scans from ADNI using CNN, Deep Learning, Federated Learning implementation.

In this work, I propose a FedACM learning Algorithm (Federated Average  Conditional Mutual Learning) to improve the performance by considering decentralized data of clients, model training by averaging the parameters learnt by each model from client after returning to server and model distillation helps learning for individual client models through mutual consensus knowledge distillation while preserving data privacy and finally conditional mutual learning helps considering the clients' local performance and the similarity between clients and mutual learning improving performance.

 Here, the method is similar to the previous approach till the pre-processing phase.Once the dataset is produced, it is divided into three datasets so that each dataset consist of only one kind of data. In this manner, the complexity of the problem is reduced. Each of the dataset is then fed into three seperate classifiers - Axial, Coronnal, Saggital(each of which is a Simple CNN Architecture).

Transfer Learning(TFL): The base 2DCNN is pre-trained on public dataset, then fine-tuned on private sample dataset.
FedAvg: The knowledge is exchanged by periodically updating the model initialization weights with the average model weights from every clients.
FedMD: The knowledge is exchanged by distillation through the average logits of each clients on public dataset. 
FedCM: To compare the effectiveness of two conditioning terms, we construct FedCM with entropy ratio conditioning.
Syft an PyTorch for FED Code

Multiple diseases detected in one software.

Decentralized data

model training by averaging the parameters

mutual consensus knowledge distillation while preserving data privacy

considers local performance and similarity to improving performance


1. User just uploads data/MRI scan and gets the predicted results in seconds. User friendly UI/UX, simple software, light weighted. Mutiple diseases detected in a single software. 

2. It is easily feasible, the disease prediction part. The federated learning is a new field and is gradually developing but companies like Google, Intel, NVIDIA have already started using it. Hence it is feasible for common.

3. Federated Learning approach with Deep learning is the uniqueness. Federated Average Conditional Mutual in Alzheimer’s Detection is the unique algorithm I developed. Federated Learning is a new field and not yet fully eveloped. With my project, it will be a step towards development of this field.
