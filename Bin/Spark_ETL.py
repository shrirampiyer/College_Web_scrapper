# -*- coding: utf-8 -*-
"""Untitled34.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zZcSuugMeK3DBTwzogmZmczLrq3FwOSY
"""

from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql.functions import upper, col
from pyspark.sql.functions import col,lit
from pyspark.sql.functions import concat
from pyspark.sql.types import IntegerType,BooleanType,DateType,DoubleType
from pyspark.sql.functions import substring

spark = SparkSession.builder.appName('Clg_analyzer').getOrCreate()

df_clg = spark.read.option('header',True).csv('/Users/Shriram/Desktop/clg_project/part-00000-8c9754c6-6b1a-41f7-92b0-141570d543b5-c000.csv')
df_clg = df_clg.withColumn("fees",df_clg.fees.cast(IntegerType()))
df_clg = df_clg.withColumn("rating",df_clg.rating.cast(DoubleType()))
df_clg = df_clg.withColumn("pkg",df_clg.pkg.cast(IntegerType()))

ap_d = spark.read.option('header',True).csv('/Users/Shriram/Desktop/clg_project/AP_DIST.csv')
ap_dist = ap_d.select('Name').rdd.flatMap(lambda x:x).collect()
ap_clg = df_clg.filter(df_clg.clg_name.rlike('|'.join(ap_dist)))
ap_clg= ap_clg.withColumn("STATE",lit('AP'))
ap_clg = ap_clg.select('*',concat(substring(ap_clg.STATE,1,2),substring(ap_clg.clg_name,1,2),substring(ap_clg.rating,1,1)).alias('CLG_ID'))
ap_clg.write.option("header",True).csv('/Users/Shriram/Desktop/clg_project/AP_CLG')

ar_d = spark.read.option('header',True).csv('/Users/Shriram/Desktop/clg_project/AR_DIST.csv')
ar_dist = ar_d.select('Name').rdd.flatMap(lambda x:x).collect()
ar_clg = df_clg.filter(df_clg.clg_name.rlike('|'.join(ar_dist)))
ar_clg = ar_clg.withColumn("STATE",lit('AR'))
ar_clg = ar_clg.select('*',concat(substring(ar_clg.STATE,1,2),substring(ar_clg.clg_name,1,2),substring(ar_clg.rating,1,1)).alias('CLG_ID'))
ar_clg.write.option("header",True).csv('/Users/Shriram/Desktop/clg_project/AR_CLG')

wb_d = spark.read.option('header',True).csv('/Users/Shriram/Desktop/clg_project/WB_DIST.csv')
wb_dist = wb_d.select('Name').rdd.flatMap(lambda x:x).collect()
wb_clg = df_clg.filter(df_clg.clg_name.rlike('|'.join(wb_dist)))
wb_clg = wb_clg.withColumn("STATE",lit('WB'))
wb_clg = wb_clg.select('*',concat(substring(wb_clg.STATE,1,2),substring(wb_clg.clg_name,1,2),substring(wb_clg.rating,1,1)).alias('CLG_ID'))
wb_clg.write.option("header",True).csv('/Users/Shriram/Desktop/clg_project/WB_CLG')

up_d = spark.read.option('header',True).csv('/Users/Shriram/Desktop/clg_project/UP_DIST.csv')
up_dist = up_d.select('Name').rdd.flatMap(lambda x:x).collect()
up_clg = df_clg.filter(df_clg.clg_name.rlike('|'.join(up_dist)))
up_clg=up_clg.withColumn("STATE",lit('UP'))
up_clg = up_clg.select('*',concat(substring(up_clg.STATE,1,2),substring(up_clg.clg_name,1,2),substring(up_clg.rating,1,1)).alias('CLG_ID'))
up_clg.write.option("header",True).csv('/Users/Shriram/Desktop/clg_project/UP_CLG')

mp_d = spark.read.option('header',True).csv('/Users/Shriram/Desktop/clg_project/MP_DIST.csv')
mp_dist = mp_d.select('Name').rdd.flatMap(lambda x:x).collect()
mp_clg = df_clg.filter(df_clg.clg_name.rlike('|'.join(mp_dist)))
mp_clg = mp_clg.withColumn("STATE",lit('MP'))
mp_clg = mp_clg.select('*',concat(substring(mp_clg.STATE,1,2),substring(mp_clg.clg_name,1,2),substring(mp_clg.rating,1,1)).alias('CLG_ID'))
mp_clg.write.option("header",True).csv('/Users/Shriram/Desktop/clg_project/MP_CLG')

gj_d = spark.read.option('header',True).csv('/Users/Shriram/Desktop/clg_project/GJ_DIST.csv')
gj_dist = gj_d.select('Name').rdd.flatMap(lambda x:x).collect()
gj_clg = df_clg.filter(df_clg.clg_name.rlike('|'.join(gj_dist)))
gj_clg = gj_clg.withColumn("STATE",lit('GJ'))
gj_clg = gj_clg.select('*',concat(substring(gj_clg.STATE,1,2),substring(gj_clg.clg_name,1,2),substring(gj_clg.rating,1,1)).alias('CLG_ID'))
gj_clg.write.option("header",True).csv('/Users/Shriram/Desktop/clg_project/GJ_CLG')

ga_d = spark.read.option('header',True).csv('/Users/Shriram/Desktop/clg_project/GOA_DIST.csv')
ga_dist = ga_d.select('Name').rdd.flatMap(lambda x:x).collect()
ga_clg = df_clg.filter(df_clg.clg_name.rlike('|'.join(ga_dist)))
ga_clg = ga_clg.withColumn("STATE",lit('GA'))
ga_clg = ga_clg.select('*',concat(substring(ga_clg.STATE,1,2),substring(ga_clg.clg_name,1,2),substring(ga_clg.rating,1,1)).alias('CLG_ID'))
ga_clg.write.option("header",True).csv('/Users/Shriram/Desktop/clg_project/GA_CLG')

as_d = spark.read.option('header',True).csv('/Users/Shriram/Desktop/clg_project/AS_DIST.csv')
as_dist = as_d.select('Name').rdd.flatMap(lambda x:x).collect()
as_clg = df_clg.filter(df_clg.clg_name.rlike('|'.join(as_dist)))
as_clg = as_clg.withColumn("STATE",lit('AS'))
as_clg = as_clg.select('*',concat(substring(as_clg.STATE,1,2),substring(as_clg.clg_name,1,2),substring(as_clg.rating,1,1)).alias('CLG_ID'))
as_clg.write.option("header",True).csv('/Users/Shriram/Desktop/clg_project/AS_CLG')

br_d = spark.read.option('header',True).csv('/Users/Shriram/Desktop/clg_project/BR_DIST.csv')
br_dist = br_d.select('Name').rdd.flatMap(lambda x:x).collect()
br_clg = df_clg.filter(df_clg.clg_name.rlike('|'.join(br_dist)))
br_clg = br_clg.withColumn("STATE",lit('BR'))
br_clg = br_clg.select('*',concat(substring(br_clg.STATE,1,2),substring(br_clg.clg_name,1,2),substring(br_clg.rating,1,1)).alias('CLG_ID'))
br_clg.write.option("header",True).csv('/Users/Shriram/Desktop/clg_project/BR_CLG')

ch_d = spark.read.option('header',True).csv('/Users/Shriram/Desktop/clg_project/CHAT_DIST.csv')
ch_dist = ch_d.select('Name').rdd.flatMap(lambda x:x).collect()
ch_clg = df_clg.filter(df_clg.clg_name.rlike('|'.join(ch_dist)))
ch_clg = ch_clg.withColumn("STATE",lit('CH'))
ch_clg = ch_clg.select('*',concat(substring(ch_clg.STATE,1,2),substring(ch_clg.clg_name,1,2),substring(ch_clg.rating,1,1)).alias('CLG_ID'))
ch_clg.write.option("header",True).csv('/Users/Shriram/Desktop/clg_project/CH_CLG')

dl_d = spark.read.option('header',True).csv('/Users/Shriram/Desktop/clg_project/DL_HIST.csv')
dl_dist = dl_d.select('Name').rdd.flatMap(lambda x:x).collect()
dl_clg = df_clg.filter(df_clg.clg_name.rlike('|'.join(dl_dist)))
dl_clg = dl_clg.withColumn("STATE",lit('DL'))
dl_clg = dl_clg.select('*',concat(substring(dl_clg.STATE,1,2),substring(dl_clg.clg_name,1,2),substring(dl_clg.rating,1,1)).alias('CLG_ID'))
dl_clg.write.option("header",True).csv('/Users/Shriram/Desktop/clg_project/DL_CLG')

hp_d = spark.read.option('header',True).csv('/Users/Shriram/Desktop/clg_project/HP_DIST.csv')
hp_dist = hp_d.select('Name').rdd.flatMap(lambda x:x).collect()
hp_clg = df_clg.filter(df_clg.clg_name.rlike('|'.join(hp_dist)))
hp_clg = hp_clg.withColumn("STATE",lit('HP'))
hp_clg = hp_clg.select('*',concat(substring(hp_clg.STATE,1,2),substring(hp_clg.clg_name,1,2),substring(hp_clg.rating,1,1)).alias('CLG_ID'))
hp_clg.write.option("header",True).csv('/Users/Shriram/Desktop/clg_project/HP_CLG')

hr_d = spark.read.option('header',True).csv('/Users/Shriram/Desktop/clg_project/HR_DIST.csv')
hr_dist = hr_d.select('Name').rdd.flatMap(lambda x:x).collect()
hr_clg = df_clg.filter(df_clg.clg_name.rlike('|'.join(hr_dist)))
hr_clg = hr_clg.withColumn("STATE",lit('HR'))
hr_clg = hr_clg.select('*',concat(substring(hr_clg.STATE,1,2),substring(hr_clg.clg_name,1,2),substring(hr_clg.rating,1,1)).alias('CLG_ID'))
hr_clg.write.option("header",True).csv('/Users/Shriram/Desktop/clg_project/HR_CLG')

jk_d = spark.read.option('header',True).csv('/Users/Shriram/Desktop/clg_project/JK_DIST.csv')
jk_dist = jk_d.select('Name').rdd.flatMap(lambda x:x).collect()
jk_clg = df_clg.filter(df_clg.clg_name.rlike('|'.join(jk_dist)))
jk_clg = jk_clg.withColumn("STATE",lit('JK'))
jk_clg = jk_clg.select('*',concat(substring(jk_clg.STATE,1,2),substring(jk_clg.clg_name,1,2),substring(jk_clg.rating,1,1)).alias('CLG_ID'))
jk_clg.write.option("header",True).csv('/Users/Shriram/Desktop/clg_project/JK_CLG')

jr_d = spark.read.option('header',True).csv('/Users/Shriram/Desktop/clg_project/JR_DIST.csv')
jr_dist = jr_d.select('Name').rdd.flatMap(lambda x:x).collect()
jr_clg = df_clg.filter(df_clg.clg_name.rlike('|'.join(jr_dist)))
jr_clg = jr_clg.withColumn("STATE",lit('JR'))
jr_clg = jr_clg.select('*',concat(substring(jr_clg.STATE,1,2),substring(jr_clg.clg_name,1,2),substring(jr_clg.rating,1,1)).alias('CLG_ID'))
jr_clg.write.option("header",True).csv('/Users/Shriram/Desktop/clg_project/JR_CLG')

ka_d = spark.read.option('header',True).csv('/Users/Shriram/Desktop/clg_project/KA_DIST.csv')
ka_dist = ka_d.select('Name').rdd.flatMap(lambda x:x).collect()
ka_clg = df_clg.filter(df_clg.clg_name.rlike('|'.join(ka_dist)))
ka_clg = ka_clg.withColumn("STATE",lit('KA'))
ka_clg = ka_clg.select('*',concat(substring(ka_clg.STATE,1,2),substring(ka_clg.clg_name,1,2),substring(ka_clg.rating,1,1)).alias('CLG_ID'))
ka_clg.write.option("header",True).csv('/Users/Shriram/Desktop/clg_project/KA_CLG')

kl_d = spark.read.option('header',True).csv('/Users/Shriram/Desktop/clg_project/KL_DIST.csv')
kl_dist = kl_d.select('Name').rdd.flatMap(lambda x:x).collect()
kl_clg = df_clg.filter(df_clg.clg_name.rlike('|'.join(kl_dist)))
kl_clg = kl_clg.withColumn("STATE",lit('KL'))
kl_clg = kl_clg.select('*',concat(substring(kl_clg.STATE,1,2),substring(kl_clg.clg_name,1,2),substring(kl_clg.rating,1,1)).alias('CLG_ID'))
kl_clg.write.option("header",True).csv('/Users/Shriram/Desktop/clg_project/KL_CLG')

mani_d = spark.read.option('header',True).csv('/Users/Shriram/Desktop/clg_project/MANI_DIST.csv')
mani_dist = mani_d.select('Name').rdd.flatMap(lambda x:x).collect()
mani_clg = df_clg.filter(df_clg.clg_name.rlike('|'.join(mani_dist)))
mani_clg = mani_clg.withColumn("STATE",lit('MANI'))
mani_clg = mani_clg.select('*',concat(substring(mani_clg.STATE,1,2),substring(mani_clg.clg_name,1,2),substring(mani_clg.rating,1,1)).alias('CLG_ID'))
mani_clg.write.option("header",True).csv('/Users/Shriram/Desktop/clg_project/MANI_CLG')

meg_d = spark.read.option('header',True).csv('/Users/Shriram/Desktop/clg_project/MEG_DIST.csv')
meg_dist = meg_d.select('Name').rdd.flatMap(lambda x:x).collect()
meg_clg = df_clg.filter(df_clg.clg_name.rlike('|'.join(meg_dist)))
meg_clg = meg_clg.withColumn("STATE",lit('MEG'))
meg_clg = meg_clg.select('*',concat(substring(meg_clg.STATE,1,2),substring(meg_clg.clg_name,1,2),substring(meg_clg.rating,1,1)).alias('CLG_ID'))
meg_clg.write.option("header",True).csv('/Users/Shriram/Desktop/clg_project/MEG_CLG')

mh_d = spark.read.option('header',True).csv('/Users/Shriram/Desktop/clg_project/MH_DIST.csv')
mh_dist = mh_d.select('Name').rdd.flatMap(lambda x:x).collect()
mh_clg = df_clg.filter(df_clg.clg_name.rlike('|'.join(mh_dist)))
mh_clg = mh_clg.withColumn("STATE",lit('MH'))
mh_clg = mh_clg.select('*',concat(substring(mh_clg.STATE,1,2),substring(mh_clg.clg_name,1,2),substring(mh_clg.rating,1,1)).alias('CLG_ID'))
mh_clg.write.option("header",True).csv('/Users/Shriram/Desktop/clg_project/MH_CLG')

miz_d = spark.read.option('header',True).csv('/Users/Shriram/Desktop/clg_project/MIZ_DIST.csv')
miz_dist = miz_d.select('Name').rdd.flatMap(lambda x:x).collect()
miz_clg = df_clg.filter(df_clg.clg_name.rlike('|'.join(miz_dist)))
miz_clg = miz_clg.withColumn("STATE",lit('MIZ'))
miz_clg = miz_clg.select('*',concat(substring(miz_clg.STATE,1,2),substring(miz_clg.clg_name,1,2),substring(miz_clg.rating,1,1)).alias('CLG_ID'))
miz_clg.write.option("header",True).csv('/Users/Shriram/Desktop/clg_project/MIZ_CLG')

nag_d = spark.read.option('header',True).csv('/Users/Shriram/Desktop/clg_project/NAG_DIST.csv')
nag_dist = nag_d.select('Name').rdd.flatMap(lambda x:x).collect()
nag_clg = df_clg.filter(df_clg.clg_name.rlike('|'.join(nag_dist)))
nag_clg = nag_clg.withColumn("STATE",lit('NAG'))
nag_clg = nag_clg.select('*',concat(substring(nag_clg.STATE,1,2),substring(nag_clg.clg_name,1,2),substring(nag_clg.rating,1,1)).alias('CLG_ID'))
nag_clg.write.option("header",True).csv('/Users/Shriram/Desktop/clg_project/NAG_CLG')

or_d = spark.read.option('header',True).csv('/Users/Shriram/Desktop/clg_project/OR_DIST.csv')
or_dist = or_d.select('Name').rdd.flatMap(lambda x:x).collect()
or_clg = df_clg.filter(df_clg.clg_name.rlike('|'.join(or_dist)))
or_clg = or_clg.withColumn("STATE",lit('OR'))
or_clg = or_clg.select('*',concat(substring(or_clg.STATE,1,2),substring(or_clg.clg_name,1,2),substring(or_clg.rating,1,1)).alias('CLG_ID'))
or_clg.write.option("header",True).csv('/Users/Shriram/Desktop/clg_project/OR_CLG')

pb_d = spark.read.option('header',True).csv('/Users/Shriram/Desktop/clg_project/PB_DIST.csv')
pb_dist = pb_d.select('Name').rdd.flatMap(lambda x:x).collect()
pb_clg = df_clg.filter(df_clg.clg_name.rlike('|'.join(pb_dist)))
pb_clg = pb_clg.withColumn("STATE",lit('PB'))
pb_clg = pb_clg.select('*',concat(substring(pb_clg.STATE,1,2),substring(pb_clg.clg_name,1,2),substring(pb_clg.rating,1,1)).alias('CLG_ID'))
pb_clg.write.option("header",True).csv('/Users/Shriram/Desktop/clg_project/PB_CLG')

rj_d = spark.read.option('header',True).csv('/Users/Shriram/Desktop/clg_project/RJ_DIST.csv')
rj_dist = rj_d.select('Name').rdd.flatMap(lambda x:x).collect()
rj_clg = df_clg.filter(df_clg.clg_name.rlike('|'.join(rj_dist)))
rj_clg = rj_clg.withColumn("STATE",lit('RJ'))
rj_clg = rj_clg.select('*',concat(substring(rj_clg.STATE,1,2),substring(rj_clg.clg_name,1,2),substring(rj_clg.rating,1,1)).alias('CLG_ID'))
rj_clg.write.option("header",True).csv('/Users/Shriram/Desktop/clg_project/RJ_CLG')

sk_d = spark.read.option('header',True).csv('/Users/Shriram/Desktop/clg_project/SK_DIST.csv')
sk_dist = sk_d.select('Name').rdd.flatMap(lambda x:x).collect()
sk_clg = df_clg.filter(df_clg.clg_name.rlike('|'.join(sk_dist)))
sk_clg = sk_clg.withColumn("STATE",lit('SK'))
sk_clg = sk_clg.select('*',concat(substring(sk_clg.STATE,1,2),substring(sk_clg.clg_name,1,2),substring(sk_clg.rating,1,1)).alias('CLG_ID'))
sk_clg.write.option("header",True).csv('/Users/Shriram/Desktop/clg_project/SK_CLG')

tr_d = spark.read.option('header',True).csv('/Users/Shriram/Desktop/clg_project/TR_DIST.csv')
tr_dist = tr_d.select('Name').rdd.flatMap(lambda x:x).collect()
tr_clg = df_clg.filter(df_clg.clg_name.rlike('|'.join(tr_dist)))
tr_clg = tr_clg.withColumn("STATE",lit('TR'))
tr_clg = tr_clg.select('*',concat(substring(tr_clg.STATE,1,2),substring(tr_clg.clg_name,1,2),substring(tr_clg.rating,1,1)).alias('CLG_ID'))
tr_clg.write.option("header",True).csv('/Users/Shriram/Desktop/clg_project/TR_CLG')

ts_d = spark.read.option('header',True).csv('/Users/Shriram/Desktop/clg_project/TS_DIST.csv')
ts_dist = ts_d.select('Name ').rdd.flatMap(lambda x:x).collect()
ts_clg = df_clg.filter(df_clg.clg_name.rlike('|'.join(ts_dist)))
ts_clg = ts_clg.withColumn("STATE",lit('TS'))
ts_clg = ts_clg.select('*',concat(substring(ts_clg.STATE,1,2),substring(ts_clg.clg_name,1,2),substring(ts_clg.rating,1,1)).alias('CLG_ID'))
ts_clg.write.option("header",True).csv('/Users/Shriram/Desktop/clg_project/TS_CLG')

uk_d = spark.read.option('header',True).csv('/Users/Shriram/Desktop/clg_project/UK_DIST.csv')
uk_dist = uk_d.select('Name').rdd.flatMap(lambda x:x).collect()
uk_clg = df_clg.filter(df_clg.clg_name.rlike('|'.join(uk_dist)))
uk_clg = uk_clg.withColumn("STATE",lit('UK'))
uk_clg = uk_clg.select('*',concat(substring(uk_clg.STATE,1,2),substring(uk_clg.clg_name,1,2),substring(uk_clg.rating,1,1)).alias('CLG_ID'))
uk_clg.write.option("header",True).csv('/Users/Shriram/Desktop/clg_project/UK_CLG')

tn_d = spark.read.option('header',True).csv('/Users/Shriram/Desktop/clg_project/TN_DIST.csv')
tn_dist = tn_d.select('Name').rdd.flatMap(lambda x:x).collect()
tn_clg = df_clg.filter(df_clg.clg_name.rlike('|'.join(tn_dist)))
tn_clg = tn_clg.withColumn("STATE",lit('TN'))
tn_clg = tn_clg.select('*',concat(substring(tn_clg.STATE,1,2),substring(tn_clg.clg_name,1,2),substring(tn_clg.rating,1,1)).alias('CLG_ID'))
tn_clg.write.option("header",True).csv('/Users/Shriram/Desktop/clg_project/TN_CLG')

clg_master = ap_clg.unionAll(up_clg)

all_df = [tn_clg,ap_clg, ar_clg, as_clg, br_clg, ch_clg, dl_clg, ga_clg, gj_clg, hp_clg, hr_clg, jk_clg, jr_clg, ka_clg, kl_clg, mani_clg, meg_clg, mh_clg, miz_clg,mp_clg,nag_clg,or_clg,pb_clg,rj_clg,sk_clg,tr_clg,ts_clg,uk_clg,up_clg,wb_clg]

resul_df = all_df[0]

for df in all_df[1:]:
    resul_df = resul_df.union(df)

resul_df.repartition(1).write.option("header",True).csv("/Users/Shriram/Desktop/clg_project/DW_CLG_MASTER")
