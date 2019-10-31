from flask_restful import Resource,fields,marshal,reqparse
from ..database.changetable import Change as ch
from ..database.db import session
from flask import request
from datetime import datetime

# 获取信息
change_fields={
    'id':fields.Integer,
    'oid':fields.Integer,
    'ctime':fields.Raw,
    'bar_codes':fields.String,
    'name':fields.String,
    'type':fields.Integer,
    'model':fields.String,
    'sn':fields.Integer,
    'unit':fields.String,
    'price':fields.String,#
    'area':fields.Integer,
    'deadline':fields.Integer,
    'supplier':fields.String,
    'linkman':fields.String,
    'tel':fields.String,
    'expir':fields.Raw,
    'info':fields.String,
    'username':fields.String,
    'companyname':fields.String,
    'departmentname':fields.String,
    'source':fields.String,
    'remark':fields.String,
    'img':fields.String
}

#时间处理函数
def EditTime(item):
    item['ctime'] = item['ctime'].strftime("%Y-%m-%d %H:%M:%S")
    item['expir'] = item['expir'].strftime("%Y-%m-%d %H:%M:%S")
    return item

# 仓库处理
def Warehouse(res):
    if res['area'] == 1:
        res['area'] = '南仓库'
    elif res['area'] == 2:
        res['area'] = "北仓库"
    return res

# 资产类型处理
def Mold(type):
    if type['type'] == 1:
        type['type'] = '电气设备'
    elif type['type'] == 2:
        type['type'] = "土地、房屋及构筑物"
    return type

class Change(Resource):
    def get(self):
        """
         变更信息
        :param oid: 变更单号
        :param ctime: 变更时间
        :param aid: 变更管理员
        :param bar_codes: 资产条码
        :param name: 资产名称
        :param type: 资产类型
        :param model: 规格型号
        :param sn: sn号
        :param unit: 计量单位
        :param price: 价位
        :param area: 存放地点，1：南仓库；2：北仓库
        :param deadline:使用期限
        :param supplier: 供应商
        :param linkman: 联系人
        :param tel: 联系方式
        :param expir: 维保到期
        :param info: 维保说明
        :return:返回所有变更信息
        """
        data = session.query(ch).all()
        for item in data:
            item.username=item.admin.username
            item.companyname=item.company.name
            item.departmentname = item.department.name
            item.source = item.property.source
            item.remark = item.property.remark
        print(data)
        # 序列号
        arr = [Mold(Warehouse(EditTime(marshal(item, change_fields)))) for item in data]
        return {"code":200,"msg":'ok','data':arr}

    # 添加
    def post(self):
        data = request.get_json(silent=True)
        print(data)
        oid = data['oid'],
        now = datetime.now()
        now = now.strftime("%Y-%m-%d %H:%M:%S")
        name = data['name']
        type = data['type']
        model = data['model']
        sn = data['sn']
        unit = data['unit']
        aid = data['aid']
        area = data['area']
        deadline = data['deadline']
        linkman = data['linkman']
        cid = data['cid']
        did = data['did']
        pid = data['pid']
        remark = data['remark']
        res = ch(oid=oid,ctime=now,name=name,type=type,model=model,sn=sn,unit=unit,aid=aid,area=area,deadline=deadline,linkman=linkman,cid=cid,did=did,pid=pid,remark=remark)
        session.add(res)
        session.commit()
        return {"code":200,"msg":'ok','data':123}
        # pass