import torch

class Utils:
    
    @staticmethod
    def run_one_epoch(model,dataloader,criterion,optimizer,is_training=True):
        model.train(is_training)

        total_loss =0
        correct_predictions=0
        images_processed=0

        with torch.set_grad_enabled(is_training):
            for images, labels in dataloader:

                if(is_training):
                    optimizer.zero_grad()

                prediction = model(images)
                loss = criterion(prediction,labels)

                if(is_training):
                    loss.backward()
                    optimizer.step()

                total_loss+= (loss.item() * images.size(0))

                predicted_classes = prediction.argmax(dim=1)
                correct_predictions+= (predicted_classes==labels).sum().item()

                images_processed+=images.size(0)

        average_loss = total_loss/images_processed
        accuracy = correct_predictions/images_processed

        return average_loss,accuracy
