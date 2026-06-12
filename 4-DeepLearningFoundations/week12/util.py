import torch
import torch.nn as nn
from baselineModel import BaselineNN
from torch.utils.data import DataLoader


class UtilHelper:
    def __init__(self):
        pass

    def _cal_accuracy(self,logits,labels):
        predictions = torch.argmax(logits, dim=1) 
        correct = (predictions == labels).sum().item()
        total = labels.size(0)
        return correct,total
    
    def train_one_epoch(self,model, train_loader, loss_fn, optimizer ):
        model.train()

        total_loss=0
        total_correct=0
        total_examples=0

        # print(f"\nTraining one epoch")
        for images, labels in train_loader:
            #Forward Pass
            logits = model(images)
            loss = loss_fn(logits, labels)
            
            #Backward pass and param update
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            #Accumulate loss
            batch_size = images.size(0)
            total_loss+= loss.item() * batch_size
            # print(f"\nbatch size {batch_size},\nloss : {loss.item()}\nTotal Loss: {total_loss}")

            #Accumulate accuracy
            correct, total = self._cal_accuracy(logits,labels)
            total_correct+=correct
            total_examples+=total
            # print(f"\ncorrect items {correct},\nTotal Correct {total_correct},\nExamples : {total}\nTotal Examples: {total_examples}")

            avg_loss = total_loss/total_examples
            avg_accuracy = total_correct/total_examples
            # print(f"\nAverage_Loss {avg_loss},\nAverage_Accuracy {avg_accuracy}")

            return avg_loss,avg_accuracy
        

    def evaluate(self, model, val_loader,loss_fn):
        model.eval()

        total_loss=0
        total_correct=0
        total_examples=0

        # print(f"\nEvaluating....")
        with torch.no_grad():
            for images,labels in val_loader:
                 #Forward Pass
                logits = model(images)
                loss = loss_fn(logits, labels)

                #Accumulate loss
                batch_size = images.size(0)
                total_loss+= loss.item() * batch_size
                # print(f"\nbatch size {batch_size},\nloss : {loss.item()}\nTotal Loss: {total_loss}")

                #Accumulate accuracy
                correct, total = self._cal_accuracy(logits,labels)
                total_correct+=correct
                total_examples+=total
                # print(f"\ncorrect items {correct},\nTotal Correct {total_correct},\nExamples : {total}\nTotal Examples: {total_examples}")

            avg_loss = total_loss/total_examples
            avg_accuracy = total_correct/total_examples
            # print(f"\nAverage_Loss {avg_loss},\nAverage_Accuracy {avg_accuracy}")

            return avg_loss,avg_accuracy


        