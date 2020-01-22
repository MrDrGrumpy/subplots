% The M code

x1 = linspace(0.0, 5.0);
x2 = linspace(0.0, 2.0);

y1 = cos(2 .* pi .* x1) .* exp(-x1);
y2 = cos(2 .* pi .* x2);

fig = figure;
title('A tale of two subplots');

subplot(2, 1, 1);
plot(x1, y1, 'o-');
ylabel('Damped oscillation');

subplot(2, 1, 2);
plot(x2, y2, '.-');
xlabel('time (s)');
ylabel('Undamped');

saveas(gcf, 'matlab_subplot.png');