#!/usr/bin/env python
# coding=utf-8

build_and_target_map = {
    'Debug'                          :'0',
    'Release'                        :'1',
    'Int Flash DDRData Debug'        :'10',
    'Int Flash DDRData Release'      :'11',
    'Int Ram Debug'                  :'12',
    'Int Ram Release'                :'13',
    'Int Flash SramData Debug'       :'14',
    'Int Flash SramData Release'     :'15',
    'Int Flash Debug'                :'16',
    'Int Flash Release'              :'17',
    'Ext MRAM Debug'                 :'18',
    'Ext Flash Debug'                :'19',
    'Ext Flash Release'              :'20',
    'Ext RAM Debug'                  :'21',
    'DDR Debug'                      :'22',
    'DDR Release'                    :'23',
    }

compiler_map = {
    'iar' :'0',
    'cw10':'1',
    'uv4' :'2',
    'cw10gcc':'3',
    'gcc_arm':'4',
    'kds':'5',
    }

software_debugger_map = {
    'iar' :'0',
    'cw10':'1',
    'uv4' :'2',
    'cw10gcc':'3',
    'lauterbach':'10',
    }

hardware_debugger_map = {
    'jlink':'0',
    'pne'  :'1',
    'lauterbach':'10',
    }
