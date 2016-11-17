program sncVacuumInterlock

int i,j,k,n;
double vacuumList_ai[20];
double vacuumList_bo[20];
double valveList_bo[4];
double rf_vc_set;
double vacuum_threshold1,vacuum_threshold2,vacuum_threshold3;

assign vacuumList_ai[0] to "SR-VA-VG1:ch2:pressure:ai";
assign vacuumList_ai[1] to "SR-VA-VG1:ch4:pressure:ai";
assign vacuumList_ai[2] to "SR-VA-VG2:ch2:pressure:ai";
assign vacuumList_ai[3] to "SR-VA-VG2:ch4:pressure:ai";
assign vacuumList_ai[4] to "SR-VA-VG3:ch2:pressure:ai";
assign vacuumList_ai[5] to "SR-VA-VG3:ch4:pressure:ai";
assign vacuumList_ai[6] to "SR-VA-VG4:ch2:pressure:ai";
assign vacuumList_ai[7] to "SR-VA-VG4:ch4:pressure:ai";
assign vacuumList_ai[8] to "SR-VA-VG5:ch2:pressure:ai";
assign vacuumList_ai[9] to "SR-VA-VG5:ch4:pressure:ai";
assign vacuumList_ai[10] to "SR-VA-VG6:ch2:pressure:ai";
assign vacuumList_ai[11] to "SR-VA-VG6:ch4:pressure:ai";
assign vacuumList_ai[12] to "SR-VA-VG7:ch2:pressure:ai";
assign vacuumList_ai[13] to "SR-VA-VG7:ch2:pressure:ai";
assign vacuumList_ai[14] to "SR-VA-VG8:ch2:pressure:ai";
assign vacuumList_ai[15] to "SR-VA-VG8:ch4:pressure:ai";
assign vacuumList_ai[16] to "SR-VA-VG9:ch2:pressure:ai";
assign vacuumList_ai[17] to "SR-VA-VG9:ch4:pressure:ai";
assign vacuumList_ai[18] to "SR-VA-VG10:ch2:pressure:ai";
assign vacuumList_ai[19] to "SR-VA-VG10:ch4:pressure:ai";


assign vacuumList_bo[0] to "SR-VA-VG1:ch2:filoff:bo";
assign vacuumList_bo[1] to "SR-VA-VG1:ch4:filoff:bo";
assign vacuumList_bo[2] to "SR-VA-VG2:ch2:filoff:bo";
assign vacuumList_bo[3] to "SR-VA-VG2:ch4:filoff:bo";
assign vacuumList_bo[4] to "SR-VA-VG3:ch2:filoff:bo";
assign vacuumList_bo[5] to "SR-VA-VG3:ch4:filoff:bo";
assign vacuumList_bo[6] to "SR-VA-VG4:ch2:filoff:bo";
assign vacuumList_bo[7] to "SR-VA-VG4:ch4:filoff:bo";
assign vacuumList_bo[8] to "SR-VA-VG5:ch2:filoff:bo";
assign vacuumList_bo[9] to "SR-VA-VG5:ch4:filoff:bo";
assign vacuumList_bo[10] to "SR-VA-VG6:ch2:filoff:bo";
assign vacuumList_bo[11] to "SR-VA-VG6:ch4:filoff:bo";
assign vacuumList_bo[12] to "SR-VA-VG7:ch2:filoff:bo";
assign vacuumList_bo[13] to "SR-VA-VG7:ch4:filoff:bo";
assign vacuumList_bo[14] to "SR-VA-VG8:ch2:filoff:bo";
assign vacuumList_bo[15] to "SR-VA-VG8:ch4:filoff:bo";
assign vacuumList_bo[16] to "SR-VA-VG9:ch2:filoff:bo";
assign vacuumList_bo[17] to "SR-VA-VG9:ch4:filoff:bo";
assign vacuumList_bo[18] to "SR-VA-VG10:ch2:filoff:bo";
assign vacuumList_bo[19] to "SR-VA-VG10:ch4:filoff:bo";


assign valveList_bo[0] to "RNG:Vacuum:Valve5:Set";
assign valveList_bo[1] to "RNG:Vacuum:Valve6:Set";
assign valveList_bo[2] to "RNG:Vacuum:Valve7:Set";
assign valveList_bo[3] to "RNG:Vacuum:Valve8:Set";

assign rf_vc_set to "SR:RF:REF:AMP:ao";

assign vacuum_threshold1 to "RNG:VACUUM:Interlock:Threshold:Vale1";
assign vacuum_threshold2 to "RNG:VACUUM:Interlock:Threshold:Vale2";
assign vacuum_threshold3 to "RNG:VACUUM:Interlock:Threshold:Vale3";

monitor vacuum_threshold1;
monitor vacuum_threshold2;
monitor vacuum_threshold3;

monitor vacuumList_ai;

ss vacuumInterlock {
	state init {
		when (delay(5.0)) {
			printf("sncVacuumInterlock: Startup delay over\n");
			printf("sncVacuumInterlock: vacuumList_ai[%d] is %2.10f !\n",19,vacuumList_ai[19]);
		} state check
	}
	state check{
		when(delay(1.0)) {
			n=0;
			for (i=0; i<20; i++)
			{
				if(vacuumList_ai[i] >= vacuum_threshold1)
				{
					/*printf("sncVacuumInterlock: vacuumList_ai[%d] is %6.2f !\n",i,vacuumList_ai[i]);*/
					rf_vc_set = 0.3;
					pvPut(rf_vc_set);
				}
				if(vacuumList_ai[i] >= vacuum_threshold2)
				{
					n=n+1;       
				}
				if(vacuumList_ai[i] >= vacuum_threshold3)
				{
					for (k = 0; k<20; k++)
					{
						vacuumList_bo[k] = 0;
						pvPut(vacuumList_bo[k]);
					}
				}
			}
			if (n >= 2)
			{
				for (j = 0; j<4; j++)
				{
					valveList_bo[j] = 0;
					pvPut(valveList_bo[j]);
				}
			}   
		}state check
	}
}

