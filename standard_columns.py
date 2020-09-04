
###############################
####### Standard Columns ######
###############################


col = "SCH_CODE_AI	SCH_NAME	SCH_NAME_L	SCH_PIN	ORG_ADDRESS	ORG_CITY	ORG_STATE	ORG_PIN	ACADEMIC_COURSE_ID	COURSE_NAME	COURSE_NAME_L	STREAM	STREAM_L	SESSION	REGN_NO	RROLL	AADHAAR_NO	CNAME	GENDER	DOB	CASTE	RELIGION	NATIONALITY	PH	MOBILE	FNAME	MNAME	GNAME	PHOTO	MRKS_REC_STATUS	SIGN	RESULT	YEAR	MONTH	DIVISION	GRADE	PERCENT	DOI	CERT_NO	SUB1NM	SUB1	SUB1MAX	SUB1MIN	SUB1_TH_MAX	SUB1_TH_MIN	SUB1_PR_MAX	SUB1_PR_MIN	SUB1_TH_MRKS	SUB1_PR_MRKS	SUB1_TOT	SUB1_STATUS	SUB1_GRADE	SUB1_GRACE	SEM	EXAM_TYPE	TOT	TOT_MRKS	TOT_MRKS_WRDS	CGPA	SGPA	SUB2NM	SUB2	SUB2MAX	SUB2MIN	SUB2_TH_MAX	SUB2_TH_MIN	SUB2_PR_MAX	SUB2_PR_MIN	SUB2_TH_MRKS	SUB2_PR_MRKS	SUB2_TOT	SUB2_STATUS	SUB2_GRADE	SUB2_GRACE	SUB3NM	SUB3	SUB3MAX	SUB3MIN	SUB3_TH_MAX	SUB3_TH_MIN	SUB3_PR_MAX	SUB3_PR_MIN	SUB3_TH_MRKS	SUB3_PR_MRKS	SUB3_TOT	SUB3_STATUS	SUB3_GRADE	SUB3_GRACE	SUB4NM	SUB4	SUB4MAX	SUB4MIN	SUB4_TH_MAX	SUB4_TH_MIN	SUB4_PR_MAX	SUB4_PR_MIN	SUB4_TH_MRKS	SUB4_PR_MRKS	SUB4_TOT	SUB4_STATUS	SUB4_GRADE	SUB4_GRACE	SUB5NM	SUB5	SUB5MAX	SUB5MIN	SUB5_TH_MAX	SUB5_TH_MIN	SUB5_PR_MAX	SUB5_PR_MIN	SUB5_TH_MRKS	SUB5_PR_MRKS	SUB5_TOT	SUB5_STATUS	SUB5_GRADE	SUB5_GRACE"

std_col = col.split() #list of standard fields

mandatory_cols = ["CNAME","FNAME","MNAME","RROLL","YEAR","REGNO"]

def checkMandatoryFields(colp):
    count = 0
    if mandatory_cols[0] not in colp:
        return mandatory_cols[0]
    if mandatory_cols[2] not in colp:
        return mandatory_cols[2]
    if mandatory_cols[3] not in colp:
        return mandatory_cols[3]
    if mandatory_cols[4] not in colp:
        return mandatory_cols[3]
    if mandatory_cols[5] not in colp:
        return mandatory_cols[5]
    if mandatory_cols[6] not in colp:
        return mandatory_cols[6]
    
    if count == len(mandatory_cols):
        return "true"
    