clc;
clear;

%% Read in data 
fileID = fopen('dirty_der.txt','r');
formatSpec = '%f'; 
A = table2array(readtable('dirty_der.txt')); 
cmd_vel =table2array(readtable('cmdvel.txt')); 
des_att = table2array(readtable('des_att.txt'));

%% What to plot/fix times 
plotk = 2;
des_att(:,1) = des_att(:,1)-cmd_vel(1,1);
cmd_vel(:,1) = cmd_vel(:,1) - cmd_vel(1,1); 
A(:,1) = A(:,1) - cmd_vel(1,1);

%% Plotting 
if plotk == 1
    subplot(3,1,1)
    plot(A(:,1),A(:,2));
    xlabel('time (s)') 
    ylabel('velocity (m/s)')
    title('x component of vel vs time') 
    subplot(3,1,2)
    plot(A(:,1),A(:,3));
    xlabel('time (s)') 
    ylabel('velocity (m/s)')
    title('y component of vel vs time')
    subplot(3,1,3)
    plot(A(:,1),A(:,4));
    xlabel('time (s)') 
    ylabel('velocity (m/s)')
    title('z component of vel vs time') 
    % Plotting numerical integration of velocity 
    %z = cumtrapz(A(:,1),A(:,2));
    %plot(A(:,1),z)
end
if plotk ==2
    subplot(2,2,1)
    plot(cmd_vel(:,1),cmd_vel(:,2))
    xlabel('time (s)')
    ylabel('Commanded Pitch')
    title('PID Control')
    
    subplot(2,2,2)
    plot(cmd_vel(:,1),cmd_vel(:,3))
    xlabel('time (s)')
    ylabel('Commanded Roll')
    title('PID Control')
    
    subplot(2,2,3)
    plot(des_att(:,1),des_att(:,2))
    xlabel('time (s)')
    ylabel('Commanded Pitch')
    title('Vel Alg')
    
    subplot(2,2,4)
    plot(des_att(:,1),des_att(:,3))
    xlabel('time (s)')
    ylabel('Commanded Roll')
    title('Vel Alg')
end 
