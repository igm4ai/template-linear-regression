import matplotlib.pyplot as plt
import torch
from torch import nn


class LinearRegression(nn.Module):
    def __init__(self):
        nn.Module.__init__(self)
{% if sys.cuda %}
        self.linear = nn.Linear(1, 1).cuda()
{% else %}
        self.linear = nn.Linear(1, 1)
{% endif %}

    def forward(self, x_):
        return self.linear(x_)


if __name__ == "__main__":
    samples = 100
    x = torch.linspace(0, 20, samples).resize_((samples, 1))  # x
    y = {{user.k}} * x + {{user.b}} + torch.randn(x.size())  # y with noise
{% if sys.cuda %}
    x, y = x.cuda(), y.cuda()
{% endif %}

    model = LinearRegression()
    criterion = nn.MSELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=1e-3)

    num_epochs = 20000
    try:
        for epoch in range(num_epochs):
            y_predict = model(x)
            loss = criterion(y_predict, y)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            if (epoch + 1) % 100 == 0:
                print('Epoch[{}/{}], loss:{:.6f}'.format(epoch + 1, num_epochs, loss.item()))
    except KeyboardInterrupt:
        pass

    fk, fb = model.linear.weight.reshape(()), model.linear.bias.reshape(())
    print(f'The fitted function is: y = {fk:.3f}x + {fb:.3f}')

    predict = model(x)
    plt.plot(x.numpy(), y.numpy(), 'ro', label='Original Data')
    plt.plot(x.numpy(), predict.data.numpy(), label='Fitting Line')
    plt.xlabel('X-Value')
    plt.ylabel('Y-Value')
    plt.title('Fitting of linear function $y = {{user.k}}x + {{user.b}}$')
    plt.show()
