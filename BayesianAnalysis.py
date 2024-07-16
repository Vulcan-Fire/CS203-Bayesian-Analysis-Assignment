import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

r = 6
n = 10

a = [2, 5, 1, 2]
b = [5, 2, 1, 2]

def beta_function(theta, a, b):
    return (theta ** (a - 1)) * ((1 - theta) ** (b - 1))

fig = make_subplots(rows=2, cols=2)

for i in range(0, 4):

    theta = np.linspace(0, 1, 10000)

    posterior = beta_function(theta, r + a[i], n + b[i] - r)

    max_index = np.argmax(posterior)
    max_theta = theta[max_index]
    max_posterior = max(posterior)

    row = i // 2 + 1
    col = i % 2 + 1

    fig.add_trace(go.Scatter(x=theta, y=posterior, mode='lines', name=f'Posterior<br>(a={a[i]}, b={b[i]})'), row=row, col=col)

    fig.add_shape(type="line", x0=r/n, y0=0, x1=r/n, y1=posterior[int(r/n*len(posterior))],
                  line=dict(color="red", width=2, dash="dash"), name='MLE',
                  row=row, col=col)
    fig.add_shape(type="line", x0=max_theta, y0=0, x1=max_theta, y1=max_posterior,
                  line=dict(color="green", width=2, dash="dash"), name='Max θ',
                  row=row, col=col)

    fig.add_trace(go.Scatter(x=[max_theta], y=[max_posterior], mode='markers',
                             marker=dict(color="blue", size=10),
                             name=f'(θ={max_theta:.2f} MAP={max_posterior*(10**6):.2f} μ)'),
                  row=row, col=col)

    fig.update_xaxes(title_text="θ", row=row, col=col)
    fig.update_yaxes(title_text="Posterior", range=[0, max_posterior*1.1], row=row, col=col)

    mean_theta = np.sum(theta * posterior) / np.sum(posterior)
    std_theta = np.sqrt(np.sum(posterior * (theta - mean_theta)**2) / np.sum(posterior))

    fig.add_vrect(x0=mean_theta, x1=mean_theta+std_theta,
                  fillcolor="rgba(249, 216, 214, 1)", layer="below", line_width=0,
                  row=row, col=col)

    fig.add_vrect(x0=mean_theta, x1=mean_theta-std_theta,
                  fillcolor="rgba(249, 216, 214, 1)", layer="below", line_width=0,
                  row=row, col=col)

    fig.add_vrect(x0=mean_theta+std_theta, x1=mean_theta+2*std_theta,
                  fillcolor="rgba(214, 205, 234, 1)", layer="below", line_width=0,
                  row=row, col=col)
    fig.add_vrect(x0=mean_theta-std_theta, x1=mean_theta-2*std_theta,
                  fillcolor="rgba(214, 205, 234, 1)", layer="below", line_width=0,
                  row=row, col=col)

    fig.add_vrect(x0=mean_theta+2*std_theta, x1=mean_theta+3*std_theta,
                  fillcolor="rgba(203, 228, 249, 1)", layer="below", line_width=0,
                  row=row, col=col)
    fig.add_vrect(x0=mean_theta-2*std_theta, x1=mean_theta-3*std_theta,
                  fillcolor="rgba(203, 228, 249, 1)", layer="below", line_width=0,
                  row=row, col=col)

    x_ticks = [0, 1, mean_theta - 3 * std_theta, mean_theta - 2 * std_theta, mean_theta - std_theta, mean_theta, mean_theta + std_theta, mean_theta + 2 * std_theta, mean_theta + 3 * std_theta]
    x_labels = ['0', '1', 'mean-3σ','mean-2σ','mean-σ','mean', 'mean+σ', 'mean+2σ', 'mean+3σ']
    fig.update_xaxes(tickvals=x_ticks, ticktext=x_labels, row=row, col=col)

    fig.add_annotation(x=r/n,y=posterior[int(r/n*len(posterior))],text='MLE',
        showarrow=True,row=row,col=col,arrowhead=1
    )

fig.update_layout(title='Plot of Posterior Function', showlegend=True, width=1400, height=1000)

fig.show()