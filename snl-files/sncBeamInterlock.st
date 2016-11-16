program sncBeamInterlock


int i,j,k;

double InjList_bo[9];
double beam_threshold,beam_curr,IVU_gap;


assign InjList_bo[0] to "SR_TM_Kick01:enable:bo";
assign InjList_bo[1] to "SR_TM_Kick02:enable:bo";
assign InjList_bo[2] to "SR_TM_Kick03:enable:bo";
assign InjList_bo[3] to "SR_TM_Kick04:enable:bo";
assign InjList_bo[4] to "SR_TM_Septum:enable:bo";
assign InjList_bo[5] to "SR_TM_Precharge:enable:bo";
assign InjList_bo[6] to "RNG:BeamStop:bo";
assign InjList_bo[7] to "IJ_TM_eGunTrigger:enable:bo";
assign InjList_bo[8] to "TM_BUCKET:If_Event_Inject:bo";


assign beam_threshold to "RNG:BEAM:INJ:Threshold";
assign beam_curr to "RNG:BEAM:CURR";
assign IVU_gap to "ivu140:EnGap_Read";

monitor beam_threshold;
monitor beam_curr;
monitor IVU_gap;

ss vacuumInterlock {
    state init {
	when (delay(5.0)) {
		printf("sncBeamInterlock: Startup delay over\n");
	} state check
    }
    state check{
	when(delay(1.0)) {
                
                if(beam_curr >= beam_threshold) 
			{
                   		/*printf("sncVacuumInterlock: vacuumList_ai[%d] is %6.2f !\n",i,vacuumList_ai[i]);*/
            	                InjList_bo[8] = 0;
                                pvPut(InjList_bo[8]);
                                delay(1.0);
		       		for (k = 0; k<8; k++)
                   		{
                       			InjList_bo[k] = 0;
                     			pvPut(InjList_bo[k]);
                   		}
		   	
			}
                if(IVU_gap <= 20)  
			{
		       		for (k = 0; k<7; k++)
                   		{
                       			InjList_bo[k] = 0;
                     			pvPut(InjList_bo[k]);
                   		}
		   	
			}
	}state check
    } 
}
