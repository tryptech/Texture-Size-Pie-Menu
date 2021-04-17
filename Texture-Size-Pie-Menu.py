import bpy
from bpy.types import Menu, Operator

# spawn an edit mode selection pie (run while object is in edit mode to get a valid output)

bl_info = {
    "name": "Texture Size Limit Pie Menu",
    "author": "tryptech",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D",
    "description": "Quickly change the viewport texture size limit from the 3D View",
    "category": "3D View",
    }

__bl_classes = []

class VIEW3D_MT_Select_Tex_Size_Menu(Menu):
    # label is displayed at the center of the pie menu.
    bl_idname = "texsize.menu"
    bl_label = "Select Texture Size Limit"

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()
        # operator_enum will just spread all available options
        # for the type enum of the operator on the pie
        
        pie.operator("texsize.4096")
        pie.operator("texsize.256")
        pie.operator("texsize.1024")
        pie.operator("texsize.none")
        pie.operator("texsize.8192")
        pie.operator("texsize.128")
        pie.operator("texsize.2048")
        pie.operator("texsize.512")

class TextureSizeNone(Operator):
    bl_idname = "texsize.none"
    bl_label = "No Limit"

    def execute(self, context):
        bpy.context.preferences.system.gl_texture_limit = 'CLAMP_OFF'

        return {'FINISHED'}

class TextureSize128(Operator):
    bl_idname = "texsize.128"
    bl_label = "128px"

    def execute(self, context):
        bpy.context.preferences.system.gl_texture_limit = 'CLAMP_128'

        return {'FINISHED'}

class TextureSize256(Operator):
    bl_idname = "texsize.256"
    bl_label = "256px"

    def execute(self, context):
        bpy.context.preferences.system.gl_texture_limit = 'CLAMP_256'

        return {'FINISHED'}

class TextureSize512(Operator):
    bl_idname = "texsize.512"
    bl_label = "512px"

    def execute(self, context):
        bpy.context.preferences.system.gl_texture_limit = 'CLAMP_512'

        return {'FINISHED'}

class TextureSize1024(Operator):
    bl_idname = "texsize.1024"
    bl_label = "1024px"

    def execute(self, context):
        bpy.context.preferences.system.gl_texture_limit = 'CLAMP_1024'

        return {'FINISHED'}

class TextureSize2048(Operator):
    bl_idname = "texsize.2048"
    bl_label = "2048px"

    def execute(self, context):
        bpy.context.preferences.system.gl_texture_limit = 'CLAMP_2048'

        return {'FINISHED'}

class TextureSize4096(Operator):
    bl_idname = "texsize.4096"
    bl_label = "4096px"

    def execute(self, context):
        bpy.context.preferences.system.gl_texture_limit = 'CLAMP_4096'

        return {'FINISHED'}
        
class TextureSize8192(Operator):
    bl_idname = "texsize.8192"
    bl_label = "8192px"

    def execute(self, context):
        bpy.context.preferences.system.gl_texture_limit = 'CLAMP_8192'

        return {'FINISHED'}

addon_keymaps = []

def register():
    bpy.utils.register_class(VIEW3D_MT_Select_Tex_Size_Menu)
    bpy.utils.register_class(TextureSizeNone)
    bpy.utils.register_class(TextureSize128)
    bpy.utils.register_class(TextureSize256)
    bpy.utils.register_class(TextureSize512)
    bpy.utils.register_class(TextureSize1024)
    bpy.utils.register_class(TextureSize2048)
    bpy.utils.register_class(TextureSize4096)
    bpy.utils.register_class(TextureSize8192)

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon

    if kc:
        km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
        kmi = km.keymap_items.new("wm.call_menu_pie", 'X', value='PRESS', alt=True)
        kmi.properties.name = "texsize.menu"
        addon_keymaps.append((km, kmi))


def unregister():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

    bpy.utils.unregister_class(TextureSizeNone)
    bpy.utils.unregister_class(TextureSize128)
    bpy.utils.unregister_class(TextureSize256)
    bpy.utils.unregister_class(TextureSize512)
    bpy.utils.unregister_class(TextureSize1024)
    bpy.utils.unregister_class(TextureSize2048)
    bpy.utils.unregister_class(TextureSize4096)
    bpy.utils.unregister_class(TextureSize8192)
    bpy.utils.unregister_class(VIEW3D_MT_Select_Tex_Size_Menu)


if __name__ == "__main__":
    register()

    bpy.ops.wm.call_menu_pie(name="texsize.menu")
