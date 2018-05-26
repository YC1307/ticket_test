# -*- coding: utf-8 -*-
"""
@author:YC1307
@file: test.py
@time：2018/5/26 14:20
"""
import re

# a = "RutWvDVs%2BFhxhozlOcgF3j9ibe12h8YppMBK0ZRJxPfKr24LfoClpc2MVE3cpCq3fYwCVGsZ27%2Fg%0AglR6KFPuEus2lQg7uzvXA%2B0ZaPOI4JS%2BOVNbSwt9GA5GxwsPvOIc7LhF8nO%2BYwIlfiZ9JFQjm4m5%0AG7okWIIsvAplzGPvhdeWD8EyIYKKuvYk8n6AR92KIvp%2FSb4mXcD%2B34USYh8UkRNwcFSQ8rF9Z%2Fss%0A8CRIlBRv3MqCn30yGN4avQNTNHZJHWlvwQ%3D%3D|预订|240000G12518|G125|VNP|AOH|VNP|AOH|11:10|16:59|05:49|Y|iOzBl3czqD6Bjc4nwHTgPc3rMfGpGU2PNDrbZiP%2By4I%2FwGhK|20180516|3|P4|01|11|1|0|||||||||||1|无|无||O0M090|OM9|0"
#
# a_re = re.search("无\|无\|无", a)
# # print(a_re.group())
# m = list
# if a_re:
#     print("票已售罄")
# else:
#     m = a.split("|")
#     print(m)
#
# # m = a.split("|")
# #
# # for i in m:
# #     print(i)
#
#
# l = [[
#          '1Yr54I7oCuoCeBVWkq5seHWlgBNagw%2B7uZoMR3SP5aEc7cyUmKtA8uAW0Q5lFbDJro9P%2B8wfz7i1%0AjNifVnKoCJnnLJaqdtiKK5FouQQxVMZNJvyGLDcfBllCf3bj1zW%2Fuug0224k3tI3CRp3N41X6jFp%0AxtoPlkqxb%2FvhVw0C5ke20IJo9QXCiUjjMgWLmYj3Ex3PNRbBZ6Qte%2FdST8k1I72njfp1AckrJqYH%0AIMFQvz7KIjhOgAcm%2BK2FBT8p9CvX',
#          '预订', '24000000G10F', 'G1', 'VNP', 'AOH', 'VNP', 'AOH', '09:00', '13:28', '04:28', 'Y',
#          'Sdm%2B%2FRmVthQucROtSp1kvTm5h09TF7%2FTb3mWHh%2BBAmftxcWC', '20180516', '3', 'P2', '01', '04', '1', '0', '',
#          '', '', '', '', '', '', '', '', '', '3', '无', '无', '', 'O0M090', 'OM9', '0'], [
#          '%2F7q8lmtPQhZ3w%2FsLL5KF%2FQhFig6becX0eCvtqca0sFaA7qVO98MwZ6dU8Z0MS59ycSRjrAD9RFLi%0AE%2BUfKX2UC6V%2FtCJVzpujAZgOCfEeTK5ksc7eTm5RbczeZDMw5MGzNqlpUf0b9bCTx1HoE70aYayi%0AQ5ZkkqkQ6qplf2V99M30DYBE8bu%2B9C%2B2bPAOKQVG2uOCKXqDkYIKMAqthnK4E7SmCc4qEVh%2BKb6p%0AE%2BF4OlgosiDsaPVIhwOanb0KRkOAQueJZg%3D%3D',
#          '预订', '2400000G410L', 'G41', 'VNP', 'HGH', 'VNP', 'AOH', '09:15', '14:49', '05:34', 'Y',
#          'OwWGlKxfnPfPYGOuhjVhioA2r3kj2krs0zxNVD04%2BIDhPhfc', '20180516', '3', 'P2', '01', '08', '1', '0', '', '', '',
#          '', '', '', '', '', '', '', '无', '1', '无', '', 'O0M090', 'OM9', '0'], [
#          'caMQuao9aCHJqUwHpFD8%2FxIeUYkaJXA1NqYn0TYoy7fd0mA%2BU9OLoApfxpvS%2FMRlXcKnFQiVbZ4F%0AfnrLfeNLRGlJ7nJtpN3YxLwUooWo6xfBbFc5aiY4ghhQTap9FgNVNXpPEW%2FHftJPMbLCOjgPiGK%2B%0ALgM3WJuWdChzIFID1zeGhtWESYN6BDQFvinyO5Uj1WIBge2xxHst5H6rIcInWTY4%2FJ3Ud67naUXY%0A9ohaiO2ejq5QKUCGReH%2FyrT6Q4wE5CH8Bw%3D%3D',
#          '预订', '240000G1170R', 'G117', 'VNP', 'AOH', 'VNP', 'AOH', '09:25', '15:37', '06:12', 'Y',
#          'Q9MiGLXizSwfSnAmRoqbslg7xobf2ecPfj4hduhmlgPC5xT3', '20180516', '3', 'P3', '01', '11', '1', '0', '', '', '',
#          '', '', '', '', '', '', '', '有', '无', '无', '', 'O0M090', 'OM9', '0'], [
#          'RutWvDVs%2BFhxhozlOcgF3j9ibe12h8YppMBK0ZRJxPfKr24LfoClpc2MVE3cpCq3fYwCVGsZ27%2Fg%0AglR6KFPuEus2lQg7uzvXA%2B0ZaPOI4JS%2BOVNbSwt9GA5GxwsPvOIc7LhF8nO%2BYwIlfiZ9JFQjm4m5%0AG7okWIIsvAplzGPvhdeWD8EyIYKKuvYk8n6AR92KIvp%2FSb4mXcD%2B34USYh8UkRNwcFSQ8rF9Z%2Fss%0A8CRIlBRv3MqCn30yGN4avQNTNHZJHWlvwQ%3D%3D',
#          '预订', '240000G12518', 'G125', 'VNP', 'AOH', 'VNP', 'AOH', '11:10', '16:59', '05:49', 'Y',
#          'iOzBl3czqD6Bjc4nwHTgPc3rMfGpGU2PNDrbZiP%2By4I%2FwGhK', '20180516', '3', 'P4', '01', '11', '1', '0', '', '',
#          '', '', '', '', '', '', '', '', '无', '无', '1', '', 'O0M090', 'OM9', '0'], [
#          'PCcITSOvcxRnkjG4abplrwDsP48PsHxiWTFSIeKaftypqB8sUv98Tt%2Fcbl6XBPuxgYUxbNeyeuHW%0AsfjYusCJomVhlmk1Z1%2B4c6opzS82FPcDzv5dmXdPgJec4iEhWlPsDtkxJzEGxJnb%2BmusVvx7gXwb%0AubaQKY5hwKp4si4y7E5rPq8AGGKDHCQ7djg6vINIvXfVHk9%2Fy4qw0jnHsmIeuR42I9mhgpGMzYp%2B%0AjnuOygkO5XaK3Ly2TQgQEV7ZspkvuHnfVw%3D%3D',
#          '预订', '240000G41107', 'G411', 'VNP', 'AOH', 'VNP', 'AOH', '11:20', '17:25', '06:05', 'Y',
#          '%2F0SOkMBPpzb1GYPfYhtbjhR5oXF2drD3o6RsTlFTBujcsoiJ', '20180516', '3', 'P2', '01', '13', '1', '0', '', '', '',
#          '', '', '', '', '', '', '', '无', '无', '6', '', 'O0M090', 'OM9', '0'], [
#          'RjFsm3llLYzwIud3wg9%2FaOOoz%2BS6zgxCiJEjwrbtTU%2BmULGextBfLIRBDppkRfvCCG5oRJYGqS0j%0A6eOXmqqLNqRqi1w0M8sA8ApS%2BZjvt%2B4JnBTcKhYqit26ttq6sm278uHK5ebJkIVCX%2FoBfgiMU70Q%0A4yzt9souPFOp99GPBWqWfJNYzKTrI8X867%2F%2Bmg3Exvm9t1QOSgUy8v%2Fk7Gmro%2F2Vdy4aLzLrBrKm%0ARe1cH0sfH2oWD%2FarVjzaX1SMvKITUs%2FliQ%3D%3D',
#          '预订', '24000014611T', '1461', 'BJP', 'SHH', 'BJP', 'SHH', '11:54', '07:19', '19:25', 'Y',
#          'M%2Bluq0W%2FeS2Hvm9PCTeQ6r4MbfdwuyXSnrIGn0U9s9Hnd0cdMyYCP%2B8cmBg%3D', '20180516', '3', 'P2', '01', '27', '0',
#          '0', '', '', '', '无', '', '', '有', '', '无', '有', '', '', '', '', '10403010', '1431', '0'], [
#          'G0rab%2FJu1jC3%2FTwJqqVRJ1FQtGVEMm9Mh6HXtb2KeiGvz33WuA07V462co9kVGD%2Fhu9%2BV3mNGszs%0AzirmOhj2ccqWzorA5lm12Ljs8EJlae8qBMRqGtZDV09%2FYwlJSHY6H29CaPzwMq%2BsJ%2BiKJ4eAuYGT%0AUEUN6FEpvr8p0UwV5FnoIBzvIUSKaDzckuDa4X3vlVWGqiigR%2FoSGU8XbXji7uIjMLlIzF%2FzFIwq%0AUo7TKslGVTlbvSBaLwGZXa3kF4vuXpaXQA%3D%3D',
#          '预订', '240000G1290T', 'G129', 'VNP', 'AOH', 'VNP', 'AOH', '12:10', '17:56', '05:46', 'Y',
#          'PqkHst0aswwEKvaCVR7Uapmm3DXK8paJmjU9NSfvbnlBvCUt', '20180516', '3', 'P4', '01', '11', '1', '0', '', '', '',
#          '', '', '', '', '', '', '', '无', '无', '3', '', 'O0M090', 'OM9', '0'], [
#          'lqUfhBFqIKOmD3zzkzMduc89SY3EgmDMufPdsMjH8ccBNDnObVqsGtfNgz5J7RGcss220O6z42%2BX%0AJaZDJ1ldbtFFiMZ3LmUA1ztQwTi%2FC9s1BSgBortIPDCR2tkdWuXvOw8qE79aNoJ09BfsCljFGLG5%0Aau%2B4YCVEUcxaQqfJyelHrfRX%2B1UQgWIg258BoBNpa3d7a01mGMyVtnSuWf99ulk7CuLuhgplc7hS%0AbfSii7c3swCN5FzwGBC%2Bl99EgRU4DkEv8A%3D%3D',
#          '预订', '240000G1310O', 'G131', 'VNP', 'AOH', 'VNP', 'AOH', '12:20', '18:10', '05:50', 'Y',
#          '1nn%2BQ1umFzzQaZfRNKPUMH01dJ4g3LJW2v2WCafHOQHTvPDC', '20180516', '3', 'P2', '01', '10', '1', '0', '', '', '',
#          '', '', '', '', '', '', '', '有', '无', '2', '', 'O0M090', 'OM9', '0'], [
#          'ySnhTASunF963TG3aM7%2BkACoapDJof0M8glmBfmhTEWDtEJrQmIAyypnDSob%2BsbcfeQEnxHGhVFT%0AYAo%2Boe0FPsLDX2VmqGBoqKH50KjhVzX1pREMJ5PiVdNuEWWzpugCLFTp9%2FsrMTBN693d7VMgNkEw%0AQQx8sYrRHQvmnKNMpVulN5phJ9Es%2Bc8rsL%2BOvEILNNcnjFN5fUT5bJO%2FaectmY0LoL5EUE04VBVn%0AibkIY8Khs3286qC4Et%2B2EYUxhnQ0xwn8FQ%3D%3D',
#          '预订', '240000G1330H', 'G133', 'VNP', 'AOH', 'VNP', 'AOH', '12:50', '18:40', '05:50', 'Y',
#          'eaISX27C%2FT247JdvbJCFWkXvFimDh4W5rNAht1O5%2F1PhCbLN', '20180516', '3', 'P3', '01', '10', '1', '0', '', '',
#          '', '', '', '', '', '', '', '', '无', '无', '2', '', 'O0M090', 'OM9', '0'], [
#          'OP48N0plwh6b4VaeOwLg%2F%2FmxW7isa6%2FyJMiuQVrDolZKx43iD1m3evAMJkkoixp%2BSpjqqKCnYGvf%0AsT3eyl6M8c5b3NRNTm4wlT8KE8cW3tHRmnZmEx9kMazqGq2mbGqrjHN1u0juzN6HnjQyjB14OIwF%0AJ9cLY%2F9PRR9dp126m6MwlT96aoL%2B%2F0dwEm1yJahJlvhX8ci0IYOE5d1K6%2FyI%2BBBLUmbjHHK2dwPU%0As5C41%2Bey%2BY0XlhOWRxI2yOhOaXos2LeoeQ%3D%3D',
#          '预订', '240000G1350D', 'G135', 'VNP', 'AOH', 'VNP', 'AOH', '13:05', '18:54', '05:49', 'Y',
#          '1OY36f%2FYc5NtxHy3DICcMYf4agZgU%2FDf6IEmXFX7a4vhxTI4', '20180516', '3', 'P4', '01', '11', '1', '0', '', '',
#          '', '', '', '', '', '', '', '', '有', '有', '2', '', 'O0M090', 'OM9', '0'], [
#          'dClA%2Bgcr8V4angEBEt814Xy%2B88CA0xKVyMA2ykInbjZ%2Bs5U1s3mbHS3UtNl24FoGctkUw6dnZcE3%0ABe%2F82ebo3MRGvPaApIM13WLa%2BmcgWjuSY%2B40nEQE2bEzuVlfl691bRBc0HlP6Pt8Evl7Wb14J2ky%0Aq0%2F8XMKbGcf8gjkgYploTFfnQlg4bgJtMdWwOM3BLic7eE9lNouYmwp61cogG1xWkUKyBI3zOHss%0A8FWPUOa2P%2BKw7ki0ZnA9ZOeJnwwy7wKY%2Fg%3D%3D',
#          '预订', '240000G1370O', 'G137', 'VNP', 'AOH', 'VNP', 'AOH', '13:35', '19:33', '05:58', 'Y',
#          'tuJZoegSzlBIXRvVyx55TJi6EyBYc4gv0OwzhxhJiPq%2FTvkf', '20180516', '3', 'P3', '01', '10', '1', '0', '', '', '',
#          '', '', '', '', '', '', '', '有', '14', '9', '', 'O0M090', 'OM9', '0'], [
#          'M1CoWP2kAqFBgyshir9LsBF9S0wAWudDEe9cQGtY5KGDDiy7y7izOncAG6AegAm1oll%2BkOnncBy0%0AfT%2Br2cKUfAo5Kn7KSYpZSqJmWjw5DqUFV3u9bBCnXUYFfzJzoag1YHbrq0wKbz%2FPREqExwwUev8C%0A%2F3ts78lRHl1SLfwx1eBbVVtd%2BTldjiq3iKJigkYYjEhTNYGeWJtYuakYcQFiA%2BWQaQBjbJTmIo7o%0AGHXRuffNkXDM1aOvts%2BK83z3%2F7iVDambvg%3D%3D',
#          '预订', '240000G1390U', 'G139', 'VNP', 'AOH', 'VNP', 'AOH', '13:45', '19:53', '06:08', 'Y',
#          'kNGQTzvS92eYeo%2BBJrESMBVa1wWAM%2Bf6L1eXfhNzv%2FcNFUIH', '20180516', '3', 'P4', '01', '12', '1', '0', '', '',
#          '', '', '', '', '', '', '', '', '有', '有', '有', '', 'O0M090', 'OM9', '0'], [
#          'iZPvgRvuya%2FmgRM4miW1wPoTcZ2bmE5JRPq0DnkLwvufczIMIUQIeii2ac1BxjjeFpJcMp0P9I3Q%0A%2FuWWE4k1rcR6cB30Nz1NCx761yKu4Gm2mNDlH%2FeE95MG6D12dS00NxNpeKoXaA0HoRdI0kod9rp%2F%0AE%2BZNxUxOXJTZ8rc058CPPZMvsQYCyMmCLq46ylxWY55rZTqR0hRDi6y4bx%2Bj7RXMXIG5YHwSyPZJ%0AtLp8Svy95zI%2BaFa0256OaocBrmfVk%2BPqBA%3D%3D',
#          '预订', '2400000G430A', 'G43', 'VNP', 'HGH', 'VNP', 'AOH', '14:05', '19:45', '05:40', 'Y',
#          'aN4AM7y5UC2De%2BhYPxBsyOZeHC39UBYIn%2BPFni6IMliIqLFy', '20180516', '3', 'P3', '01', '09', '1', '0', '', '',
#          '', '', '', '', '', '', '', '', '无', '2', '3', '', 'O0M090', 'OM9', '0'], [
#          'y%2Bh47XJv%2BGHUUhi7l2Z553skU5aNYQMZsBoTrTRhCU1IDSvxefUh9j5ky30SE5KuLucxxnmv2ifE%0Aoi%2BcTi1oduMtfNztadJNgEPBa2OP81Z73RMrmOx8Nw7h7ojgJuJcR8FIYf9ukct0fuvjj%2BkNsoUE%0A0tedfWh3rpD9lHiTxQVQFYJW0g1TW3rZYotP8qtmWPqkWcwh5CjsyZ%2FuTu3aV%2BNpMznI7OQvbkx3%0AHxDnPnIGzjXG%2FbbgHy03rtc5ynFs9KFS0Q%3D%3D',
#          '预订', '240000G1410H', 'G141', 'VNP', 'AOH', 'VNP', 'AOH', '14:10', '20:05', '05:55', 'Y',
#          'INDob%2FMKpstFDEz0j%2BGbUIyZt23g0iwx%2BMHFnqqzt%2FQIJwxu', '20180516', '3', 'P2', '01', '11', '1', '0', '',
#          '', '', '', '', '', '', '', '', '', '有', '有', '10', '', 'O0M090', 'OM9', '0'], [
#          'wmwzCkKquiRfJRNtWBU8ZTorbYGEzUJAE%2BD32%2B4E3BTV2wJAO1mmVP5gyoVTspOfSlxVyXc3UAh6%0ARyf47Kq7c8tDQD4Zd7OuqsHBP97PrrpiEPDmJicbz3Ch2HVk2kChSzsc2g1wBCMPNABwB7zJFIdE%0AJuOVGyZ94d468UYKMg3cE4EP4DS7434cXLETZzun2ZPixWX81ihEN1RKyR9nRw1LdUea%2BZvmhg%2Bo%0A0WxkCATp8XWIkvzHzdNfgl1hkPwtBrp4vw%3D%3D',
#          '预订', '240000G1450P', 'G145', 'VNP', 'AOH', 'VNP', 'AOH', '14:35', '20:34', '05:59', 'Y',
#          'a3NVlOIPCZQJ7FECCln46LL3Q%2F1bExWJmrBP3tdXo2QMOQ7R', '20180516', '3', 'P4', '01', '10', '1', '0', '', '', '',
#          '', '', '', '', '', '', '', '有', '有', '无', '', 'O0M090', 'OM9', '0'], [
#          'pjZCh0l%2BQ%2B%2BmnKEUsPMmZ13GWh5caX%2F5jgdx4DO0jF6n0gj%2Bss7hrqMKYitYAA%2BVlDygMsyUDO7P%0Am53cbrXdYvz3bGr7VuqIzaKCjC3RxJjpStx8nTmTM%2B3a%2FKrae8i0u4v0RRW6WObJVlj%2BJMQZ52Qw%0AcNuWm8CCTMMPvhJzl4%2Fjbph%2BmGtYqfE2aViPqtXB2SZpT%2BAs3SyOF6Jr86g5okaHWQVaOsElUVB0%0AapYX1Hl8mqlXvDgoReV2F5eZ9t6diop1Gw%3D%3D',
#          '预订', '240000G1551U', 'G155', 'VNP', 'AOH', 'VNP', 'AOH', '15:45', '21:41', '05:56', 'Y',
#          'K5I9HxfcYku%2FWBAfPJGbQWuciERwXhRupQhon64CWTxyv2jf', '20180516', '3', 'P4', '01', '10', '1', '0', '', '', '',
#          '', '', '', '', '', '', '', '有', '有', '11', '', 'O0M090', 'OM9', '0'], [
#          '52uX4sNipDnb1NN40eEHSyvsW1rcJSHExwpY9PT9ZeUyeL4IRca2qg5LEJkFifvcl7WqoEA462nu%0A5QCAefe8Nhzdx0K61FOt%2FRABHyqbAlW6w4o55yjPxzgfG0oseQFBWh%2FWwdNeV%2B21zCDfNWl403gf%0AObjVlY1DVOpXROyePZCPEicri2mwa%2BzGSeXNg7qAsKS9owFtEGWtqQ%2BBDEhfjVa5PYl3maNa7vDX%0AU4rIM7puiVbQLgpsF%2B8parJwJ81eJcxOHA%3D%3D',
#          '预订', '240000G1470D', 'G147', 'VNP', 'AOH', 'VNP', 'AOH', '15:50', '22:00', '06:10', 'Y',
#          'BBMm7fGi5i1QboNQ2yfhfruZF2fP8fykFumt%2FGRaosqF%2FHQl', '20180516', '3', 'P3', '01', '12', '1', '0', '', '',
#          '', '', '', '', '', '', '', '', '有', '有', '有', '', 'O0M090', 'OM9', '0'], [
#          'PLdbDjL%2F%2F1tp8EardxUndx8V%2BVQD8Eg9nZWCL%2BoU1%2F6R56YyTb%2FZRXeRzNlwjR0NB6xP3GiPbEfS%0A0yl9AOT%2FtilkmQh6gQ%2BtcZ8Q0tRyhmpspWXVgj6nJ70ysSAnNrRhvylXZfIXQcJd72WHIUMTJeoq%0AvgXHADr%2F%2BqePVI4Ig3nKuOPDZGCJiR%2FJmXO%2Bn35ewKJF6NT5%2FESKHlIeq8iqT3Yzuk0FgzuNSVT9%0A%2FHOH5upXgez1xe5x3QLiEHQo09FESdeeCQ%3D%3D',
#          '预订', '240000G16900', 'G169', 'VNP', 'AOH', 'VNP', 'AOH', '16:40', '22:42', '06:02', 'Y',
#          'NdM9GWBV27gJE15SalxAuASGeiRIgUHdYmGVgfrKkx5Mf7F6', '20180516', '3', 'P4', '01', '10', '1', '0', '', '', '',
#          '', '', '', '', '', '', '', '有', '有', '19', '', 'O0M090', 'OM9', '0'], [
#          'jwmj84EH5CbtLTynWtBPbAqn9Z4vWlqO1N50%2Fjp%2BsM8YkiH78ooOoC9yWuZ8POxVFfc5xQBeqRvZ%0AeLdEfZJgdUXGWGqKyWJDcKq7GVP2j%2B7TrE%2F6T9Z5riTblPFdbD7koNomIeU16NR2ymh4KIEiezv7%0AtrylNTj8wN%2BLqftEu74iK1fEKizHJr8G1p2YffwwVJH0MknYy326112Sphi4iLb0qQEEDc7ky7BK%0A2FMxSFhcpNIBTfdjRM99PPcrYDaCQ2TaLw%3D%3D',
#          '预订', '240000G1512N', 'G151', 'VNP', 'AOH', 'VNP', 'AOH', '16:45', '23:02', '06:17', 'Y',
#          'ZWqL3%2BzbzYSiSJUWNMIlRq06j9AAgW%2FF1RaBpp41k%2BujYwxc', '20180516', '3', 'P2', '01', '13', '1', '0', '', '',
#          '', '', '', '', '', '', '', '', '有', '有', '20', '', 'O0M090', 'OM9', '0'], [
#          '6ogtOMl9BwCRTooapv4xxxvqIwFuAbmhAxieAfulMH89neLqOxVhI2Net%2FSg6wNZLbfU%2FSO9KVNx%0AFBrSTNYoNeScz6PQiT4a0Fdlt%2BluzrVCZZxs72ZiH2hvu7CKbg4VB8TiInlXPEUc4NsN6qQFqb0t%0A7FKUDDCPSqJCkucjXrNvzxM2EAXruK2qvg6nj%2FB0qJ4eyRwlJm32kd%2BtMTNoUcUb9gk8bmAR2%2FCR%0AhNKAWBK%2B3lr01Z6zbWFxkguPzNhW3sG5pQ%3D%3D',
#          '预订', '240000G1530F', 'G153', 'VNP', 'AOH', 'VNP', 'AOH', '17:15', '23:11', '05:56', 'Y',
#          'yILl1EJG2TjVe5DCdmTW4hnJtFuOz3zXwLTnqKBigc9tNF%2Bt', '20180516', '3', 'P3', '01', '11', '1', '0', '', '', '',
#          '', '', '', '', '', '', '', '有', '有', '有', '', 'O0M090', 'OM9', '0'], [
#          'iwJIv33kAZmYUz4vFI7UkuRc85foW0Drs2LojH%2FPPJ8slLJ9nFs1HXTd6qH63AoZDuJ3d1fNvbV4%0ARiGf%2BIWk5B3Ga3lw47bQoS%2BbKMIVVcnhacTPLq1cUzqrg8GB6Q7REPyFHu%2Bsedkc8C3VJUJMlI1w%0AWLN%2F4H%2FdiskIW46ZgGqpGKZnM1BvMpUdzeyFRNcxJbI5uUaYRFkQojpqS%2BD%2FfuZ6%2FjZXhhEAqIJq%0AAY09LCCrhCdFV8utTB%2FhEE8RRaf9UHzObw%3D%3D',
#          '预订', '240000G1570L', 'G157', 'VNP', 'AOH', 'VNP', 'AOH', '17:36', '23:40', '06:04', 'Y',
#          'FsXZkNANTPxhSge%2F9G9vRpQv3EvBCoBdOibtYISE5ev0zE5e', '20180516', '3', 'P3', '01', '10', '1', '0', '', '', '',
#          '', '', '', '', '', '', '', '有', '有', '16', '', 'O0M090', 'OM9', '0'], [
#          'toK4v8qVu4J1DZHKsviivbiY7sqgaXSOTbSwgQ7fjOXmXiDKgBWClgY30zzG1YIGkypCBrS6PR1x%0AfaTMDAJ2yE1PEt5Zgn2RNH9oVj58cgoLSXCNXu3S%2FbHMZT9at87NfRCEZTnwruM%2BCZ3A0iBmpX1q%0ApniZ3DgpbEqfCy7mB1D1H7jPxFIwfiT7GQxMIBf1uYv2iaGs8Qql3hC7L8T90oGpnNqfFdzdi%2F%2BK%0A1z%2F%2BVE7bfciDFH3uuxv02luvu%2Fa%2BXXpb9w%3D%3D',
#          '预订', '2400000G150D', 'G15', 'VNP', 'AOH', 'VNP', 'AOH', '18:00', '22:36', '04:36', 'Y',
#          '5hSeamefr1hE1jrBgMtwsVab3YJDk45NZctS%2B%2FMf66UpgwJD', '20180516', '3', 'P4', '01', '05', '1', '0', '', '',
#          '', '', '', '', '', '', '', '', '18', '无', '8', '', 'O0M090', 'OM9', '0'], [
#          '5Imcx2opPsulzp6jcONp%2BzhzJ%2FapzyLbk0rilSyoIAO1wg39eJ3oaut7EXwJHMbYa%2FafsbiFw8UH%0ARSmxhMjVU67hsxrG%2BImI7%2BFwsGxakogwHWk3gMRslU%2BdgOCi19p%2FYknhJQZm3rRb88Qg9r79M%2BOn%0AwARivQMIPAXehgCidSbHyQto2oXTcpvyuYRVC08BCFRXZFpM%2FT30E%2F37nY7qdkPZsJ1vLm9Djdx7%0ADVIjWdm%2FABANo2oFTojk%2FUhO6tZFzycAUg%3D%3D',
#          '预订', '2400000G170A', 'G17', 'VNP', 'AOH', 'VNP', 'AOH', '19:00', '23:18', '04:18', 'Y',
#          '%2FUpURMgzkgSioh432NUW6tAZh7UbAuSnXqnQJA7sf6nwPgdQ', '20180516', '3', 'P3', '01', '03', '1', '0', '', '', '',
#          '', '', '', '', '', '', '', '有', '无', '无', '', 'O0M090', 'OM9', '0'], [
#          'Lx6wZufeClrMGeS%2BlEpO%2BRm%2F7QCrndeAz8HGF4qj6cSI6nuur4CN5jSlsignX%2FdM8OKGc1jaDofo%0AIbd5%2F9EIaZM%2F5yHUkpRhJfy1567TNRk4wYS0Mfu2Z9OrWBjWnixcXa%2BIqcxBo1R3sck5NewQtfgj%0ACE6pCUNKc%2BaQCPje7nUwNEczPWEEj6mUpPxhhX8RSPtZkjmwWSN4qK1bnKD23jT9FfM%2FAMgie0ZT%0ATqz7E4eebXIIlVtVjCBUUxg%3D',
#          '预订', '2400000G2100', 'G21', 'VNP', 'SHH', 'VNP', 'SHH', '19:08', '23:36', '04:28', 'Y',
#          'IMnwV2Jiz8FFqlToVOmnzsO4IvLTWyLIfYjSTkux7G4eazMb', '20180516', '3', 'P2', '01', '04', '1', '0', '', '', '',
#          '', '', '', '', '', '', '', '有', '无', '4', '', 'O0M090', 'OM9', '0'], [
#          'wJujdfR9NTxfdAIJG2mdlmsvIGxlfVfsT9Vcivg%2FmlTCJgpJ5KWRP3ZPVBmLMUFN7TizYsJQ%2FqDk%0A16wBbmTEoddxOm0XKtvHtJ5W7SGvMjiWkwq2lDJZkW48T6YaflU079R6HJ532jnQVfCSMaL2mdzl%0AiqH8RgCRsJEWE%2FQikSObt3VI8AddyZ747O5z%2B3CuRoEmvEus9APJQ8GIQBWYfALg4PwGW7D46PiY%0AQgAlGBMDGVb7tTcMo%2Fg%2FzmMUAOWl6zTGActW4rB5CEejZyhL1A%3D%3D',
#          '预订', '240000T10910', 'T109', 'BJP', 'SHH', 'BJP', 'SHH', '19:30', '10:43', '15:13', 'Y',
#          '5BiYxxfvl%2Fq6RUBGOmLdGhDjJ%2FrmCI16XnE2ACHF7mx%2Fx5J4PNMUuxo%2BcTYmQKWiV1SoMpSJyMk%3D', '20180516', '3',
#          'P4', '01', '09', '0', '0', '', '4', '', '无', '', '', '有', '', '无', '有', '', '', '', '', '1040601030', '14613',
#          '0'], [
#          'wpglsV6Zw0sT8xOHh0fmXTIEqcKw9O0SB8%2FpC%2BYuZVntwm42VWGumQxYOpzCjpL1q3WdZ4rowRen%0ASEZvkvT6%2FFoKEMFMdHUGKzIWGETH3FnIzlMduXtAGBwAWZc2YLiPc3IEt63F7htyHoqTWAUJHTtW%0A%2BUrfeiomeVvDnxyHqcK1alQ5fstc6STdwFlQ0pfwmqOQbTaaZwPPQj3dvxs1A6czmFWKqY4571bD%0AsETqNGXBiv42TTrTXZEZHWI%3D',
#          '预订', '240000D3130U', 'D313', 'VNP', 'SHH', 'VNP', 'SHH', '19:34', '07:41', '12:07', 'Y',
#          'ivzB1d2NtGb4zY8IsRsKyGHczl2wsJOghb7lS1S4EdqQVrK1', '20180516', '3', 'P3', '01', '05', '0', '0', '', '', '',
#          '有', '', '', '16', '', '', '', '无', '', '', '', 'O0O040', 'OO4', '0'], [
#          'dCCoilWaCKv%2BChDXmm%2FX2SIxt92pct1TppsLce5%2FCaonUu%2FAHvRhayrflXuMgYEJRQyIhJn1jfje%0AR%2ByZO32THFAV75A6Jjc8zxDv3MWXn019ZG0UPSoiQlS94JRHeDGR8caDiI6Rqd%2BKNRnuapOOlX2d%0AI%2BIgGwZdT9SThZn%2BtviCIttoCawe8YDpwQJmO2XdVDesAnE%2FJM4ddQQTaSqMXYj2aRReFQQr%2Ftl0%0AK6OgiRMDHQXN',
#          '预订', '240000D3110K', 'D311', 'VNP', 'SHH', 'VNP', 'SHH', '21:11', '09:09', '11:58', 'Y',
#          'd2nFKx05mvNpsIkKzdGeu0841t8Hyab7', '20180516', '3', 'P2', '01', '05', '0', '0', '', '', '', '无', '', '', '',
#          '', '', '', '', '', '', '有', 'F040', 'F4', '0'], [
#          'aQ1TvOG3u7j09UeVvA8dimF5a%2BlQ%2FM2rsCOlvhRzRcyxkjUxb9HgDQI4uywQ0L%2BImJsgCNXwzhKI%0A3lL3lszDL9o6zEEpCOyI%2BXNsV6eatv8PUwikiMHSXCTL3PIXxRkzYaQ1iDVcbO2e9b19QO%2FtOtwH%0AXWNe1KsuVazcViSsD1hE%2F6x%2FKC9vw9PT8lslA59z8AXOXO4a7jTalGt5Q3HzpgBcm3KuNJieEUZy%0AefOAnaaYBUf8v4nNRfqRuq4%3D',
#          '预订', '240000D3210D', 'D321', 'VNP', 'SHH', 'VNP', 'SHH', '21:23', '09:15', '11:52', 'Y',
#          'QOriwk53bNZmjP09PdOV3vgDsVY4u6slwFlApQxKJFnIJQin', '20180516', '3', 'P2', '01', '04', '0', '0', '', '', '',
#          '有', '', '', '14', '', '', '', '1', '', '', '', 'O0O040', 'OO4', '0']]





new_l = [
         '1Yr54I7oCuoCeBVWkq5seHWlgBNagw%2B7uZoMR3SP5aEc7cyUmKtA8uAW0Q5lFbDJro9P%2B8wfz7i1%0AjNifVnKoCJnnLJaqdtiKK5FouQQxVMZNJvyGLDcfBllCf3bj1zW%2Fuug0224k3tI3CRp3N41X6jFp%0AxtoPlkqxb%2FvhVw0C5ke20IJo9QXCiUjjMgWLmYj3Ex3PNRbBZ6Qte%2FdST8k1I72njfp1AckrJqYH%0AIMFQvz7KIjhOgAcm%2BK2FBT8p9CvX',
         '预订', '24000000G10F', 'G1', 'VNP', 'AOH', 'VNP', 'AOH', '09:00', '13:28', '04:28', 'Y',
         'Sdm%2B%2FRmVthQucROtSp1kvTm5h09TF7%2FTb3mWHh%2BBAmftxcWC', '20180516', '3', 'P2', '01', '04', '1', '0', '',
         '', '', '', '', '', '', '', '', '', '3', '无', '无', '', 'O0M090', 'OM9', '0']
len()
