/*
 * Data: 19/03/2019 
 * 5º Semestre - Engenharia da Computação - Insper
 * Marco Mello - marcoasma@insper.edu.br
 */

#ifndef keypad_LabArqComp_H_INCLUDED
#define keypad_LabArqComp_H_INCLUDED

#include "asf.h"

#define KEY_LIN_1				PIOD
#define KEY_LIN_1_ID			ID_PIOD
#define KEY_LIN_1_IDX			30
#define KEY_LIN_1_IDX_MASK (1 << KEY_LIN_1_IDX)

#define KEY_LIN_2				PIOA
#define KEY_LIN_2_ID			ID_PIOA
#define KEY_LIN_2_IDX			6
#define KEY_LIN_2_IDX_MASK (1 << KEY_LIN_2_IDX)

#define KEY_LIN_3				PIOC
#define KEY_LIN_3_ID			ID_PIOC
#define KEY_LIN_3_IDX			19
#define KEY_LIN_3_IDX_MASK (1 << KEY_LIN_3_IDX)

#define KEY_LIN_4				PIOA
#define KEY_LIN_4_ID			ID_PIOA
#define KEY_LIN_4_IDX			2
#define KEY_LIN_4_IDX_MASK (1 << KEY_LIN_4_IDX)

#define KEY_COL_1				PIOA
#define KEY_COL_1_ID			ID_PIOA
#define KEY_COL_1_IDX			3
#define KEY_COL_1_IDX_MASK (1 << KEY_COL_1_IDX)

#define KEY_COL_2				PIOA
#define KEY_COL_2_ID			ID_PIOA
#define KEY_COL_2_IDX			21
#define KEY_COL_2_IDX_MASK (1 << KEY_COL_2_IDX)

#define KEY_COL_3				PIOD
#define KEY_COL_3_ID			ID_PIOD
#define KEY_COL_3_IDX			27
#define KEY_COL_3_IDX_MASK (1 << KEY_COL_3_IDX)

#define KEY_COL_4				PIOD
#define KEY_COL_4_ID			ID_PIOD
#define KEY_COL_4_IDX			20
#define KEY_COL_4_IDX_MASK (1 << KEY_COL_4_IDX)

#endif



