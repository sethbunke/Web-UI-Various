class DecoderRNN(nn.Module):
    
    def __init__(self, embed_size, hidden_size, vocab_size, num_layers=1, drop_prob=0.0):

        super(DecoderRNN, self).__init__()

        self.embed = nn.Embedding(vocab_size, embed_size)  
        self.lstm = nn.LSTM(input_size=embed_size, hidden_size=hidden_size, num_layers=num_layers, dropout=drop_prob)   
        self.linear = nn.Linear(hidden_size, vocab_size)

     
    def forward(self, features, captions):

        features = features.view(len(features), 1, -1)

        embeddings = self.embed(captions[:, :-1])

        inputs = torch.cat((features, embeddings), 1)        
        out, hidden = self.lstm(inputs)

        out = self.linear(out)

        return out



    def sample(self, features, states=None, max_len=20):

        for i in range(max_len):

            if states is None:

                inputs = features        
            else:     
                embeddings = self.embed(states)

                inputs = torch.cat((features, embeddings), 1)

                 
            lstm_out, hidden = self.lstm(inputs)

            out = self.linear(lstm_out)

            val, states = out.max(2)

                 
        output = states.tolist()[0]

        return output


#         I tried Adam and SGD optimisers, one and two LSTM layers, 256 and 512 sizes for embedded and hidden sizes, batch size 100 and 200.

# It all runs with no errors. Loss starts from 7-9, quickly goes to 3 where it stays very slowly decreasing.

# The problem is with predictions after training 1 or 2 epochs. For any image I get the same output: "a man is a man is a man is a man...".

# Could you suggest what is a mistake and how to fix it? Thank you