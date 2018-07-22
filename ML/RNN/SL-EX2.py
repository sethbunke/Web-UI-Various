forward() method look like? Here's mine:
    
>    def forward(self, features, captions):      
>        embeds = self.word_embeddings(captions[:,:-1])
>        inputs = torch.cat((features.unsqueeze(1),embeds),1)
>        lstm_out, hidden = self.lstm(inputs)
>        out = self.linear(lstm_out)
>        return out







Hey @Isara Rungvitayakul, my model uses just 1 lstm layer, with 256 embed size, and 512 hidden size, Adam optimizer, and 256 batch size. I know that my model is under capacity, and it only produces a single word all the time. However, I'm surprised that my perplexity is pretty close to one (and this is before completing the first epoch). I'm unable to debug the issue. Any help here?






Hi @Weina ,

My model structure using 256 for embeds and 512 for hidden layers. 3 layers of lstm.

i had train with 512 on both embedding and hidden layer once. But it suffer from the same output as well, then i lower the the embeds layer to 256. And it generate difference outout.

IMO, if we have equal number of embedding layer compare to the hidden layer, lstm seem not remembering the previous seen value. I don't know why.. just from my trial and error.








Hi @Weina ,

My model structure using 256 for embeds and 512 for hidden layers. 3 layers of lstm.

i had train with 512 on both embedding and hidden layer once. But it suffer from the same output as well, then i lower the the embeds layer to 256. And it generate difference outout.

IMO, if we have equal number of embedding layer compare to the hidden layer, lstm seem not remembering the previous seen value. I don't know why.. just from my trial and error.


#########
#MULTIPLY OUTPUT POINTS BY -1 TO SHIFT THEM OVER

# github repo
# https://github.com/physicsman/Udacity_CVND