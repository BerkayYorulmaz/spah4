clear
clc
close all

addpath('.\matlab_files')

mask = import_2Dmask('.\map_files\mask_1km.asc');

obs = import_2Dmap('.\map_files\obs.asc');
sim = import_2Dmap('.\map_files\sim_1.asc');

obs(mask(:,:)==0)=NaN;
sim(mask(:,:)==0)=NaN;

obs_vec=obs(~isnan(obs));
sim_vec=sim(~isnan(sim));



[ spah4_1, alpha1, beta1, gamma1, kappa1 ] = SPAH4_func( sim_vec,obs_vec );

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
obs = import_2Dmap('.\map_files\obs.asc');
sim = import_2Dmap('.\map_files\sim_2.asc');

obs(mask(:,:)==0)=NaN;
sim(mask(:,:)==0)=NaN;

obs_vec=obs(~isnan(obs));
sim_vec=sim(~isnan(sim));

[ spah4_2, alpha2, beta2, gamma2, kappa2 ] = SPAH4_func( sim_vec,obs_vec );

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
obs = import_2Dmap('.\map_files\obs.asc');
sim = import_2Dmap('.\map_files\sim_3.asc');

obs(mask(:,:)==0)=NaN;
sim(mask(:,:)==0)=NaN;

obs_vec=obs(~isnan(obs));
sim_vec=sim(~isnan(sim));

[ spah4_3, alpha3, beta3, gamma3, kappa3 ] = SPAH4_func( sim_vec,obs_vec );

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
obs = import_2Dmap('.\map_files\obs.asc');
sim = import_2Dmap('.\map_files\sim_4.asc');

obs(mask(:,:)==0)=NaN;
sim(mask(:,:)==0)=NaN;

obs_vec=obs(~isnan(obs));
sim_vec=sim(~isnan(sim));



[ spah4_4, alpha4, beta4, gamma4, kappa4 ] = SPAH4_func( sim_vec,obs_vec );

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
obs = import_2Dmap('.\map_files\obs.asc');
sim = import_2Dmap('.\map_files\sim_5.asc');

obs(mask(:,:)==0)=NaN;
sim(mask(:,:)==0)=NaN;

obs_vec=obs(~isnan(obs));
sim_vec=sim(~isnan(sim));


[ spah4_5, alpha5, beta5, gamma5, kappa5 ] = SPAH4_func( sim_vec,obs_vec );

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
obs = import_2Dmap('.\map_files\obs.asc');
sim = import_2Dmap('.\map_files\sim_6.asc');

obs(mask(:,:)==0)=NaN;
sim(mask(:,:)==0)=NaN;

obs_vec=obs(~isnan(obs));
sim_vec=sim(~isnan(sim));


[ spah4_6, alpha6, beta6, gamma6, kappa6 ] = SPAH4_func( sim_vec,obs_vec );

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
obs = import_2Dmap('.\map_files\obs.asc');
sim = import_2Dmap('.\map_files\sim_shuffled.asc');

obs(mask(:,:)==0)=NaN;
sim(mask(:,:)==0)=NaN;

obs_vec=obs(~isnan(obs));
sim_vec=sim(~isnan(sim));


[ spah4_7, alpha7, beta7, gamma7, kappa7 ] = SPAH4_func( sim_vec,obs_vec );

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
obs = import_2Dmap('.\map_files\obs.asc');
sim = import_2Dmap('.\map_files\obs.asc');

obs(mask(:,:)==0)=NaN;
sim(mask(:,:)==0)=NaN;

obs_vec=obs(~isnan(obs));
sim_vec=obs_vec*1.4;


[ spah4_8, alpha8, beta8, gamma8, kappa8 ] = SPAH4_func( sim_vec,obs_vec );

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
obs = import_2Dmap('.\map_files\obs.asc');
sim = import_2Dmap('.\map_files\obs.asc');

obs(mask(:,:)==0)=NaN;
sim(mask(:,:)==0)=NaN;

obs_vec=obs(~isnan(obs));
sim_vec=obs_vec+2;


[ spah4_9, alpha9, beta9, gamma9, kappa9 ] = SPAH4_func( sim_vec,obs_vec );

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
obs = import_2Dmap('.\map_files\obs.asc');
sim = import_2Dmap('.\map_files\obs.asc');

obs(mask(:,:)==0)=NaN;
sim(mask(:,:)==0)=NaN;

obs_vec=obs(~isnan(obs));
sim_vec=obs_vec.^2;


[ spah4_10, alpha10, beta10, gamma10, kappa10 ] = SPAH4_func( sim_vec,obs_vec );

fileID = fopen('.\results\SPAH4_results.txt','w');
fprintf(fileID,'%5s %5s \r\n','ID','SPAH4') 
fprintf(fileID,'%3s %.6f \r\n','Case1', spah4_1 ,'Case2',spah4_2,'Case3',spah4_3,'Case4',spah4_4,'Case5',spah4_5,'Case6',spah4_6,'Case7',spah4_7,'Case8',spah4_8,'Case9',spah4_9,'Case10',spah4_10);


