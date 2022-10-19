import platform

from setuptools import Extension, setup


def get_ext_modules() -> list:
    """
    获取三方模块
    Windows需要编译封装接口
    Mac和Linux由于缺乏二进制库支持无法使用
    """
    # if platform.system() == "Linux":
    #     extra_compile_flags = [
    #         "-std=c++17",
    #         "-O3",
    #         "-Wno-delete-incomplete",
    #         "-Wno-sign-compare",
    #     ]
    #     extra_link_args = ["-lstdc++"]
    #     runtime_library_dirs = ["$ORIGIN"]

    if platform.system() == "Windows":
        extra_compile_flags = ["-O2", "-MT"]
        extra_link_args = []
        runtime_library_dirs = []

    else:
        return []

    # vnctpmd = Extension(
    #     name="vnpy_jees.api.vnctpmd",
    #     sources=["vnpy_jees/api/vnctp/vnctpmd/vnctpmd.cpp"],
    #     include_dirs=["vnpy_jees/api/include", "vnpy_jees/api/vnctp"],
    #     library_dirs=["vnpy_jees/api/libs", "vnpy_jees/api"],
    #     libraries=["thostmduserapi_se", "thosttraderapi_se"],
    #     extra_compile_args=extra_compile_flags,
    #     extra_link_args=extra_link_args,
    #     runtime_library_dirs=runtime_library_dirs,
    #     language="cpp",
    # )

    vnjeestd = Extension(
        name="vnpy_jees.api.vnjeestd",
        sources=["vnpy_jees/api/vnjees/vnjeestd/vnjeestd.cpp"],
        include_dirs=["vnpy_jees/api/include", "vnpy_jees/api/vnjees"],
        library_dirs=["vnpy_jees/api/libs", "vnpy_jees/api"],
        libraries=["thosttraderapi_se"],
        extra_compile_args=extra_compile_flags,
        extra_link_args=extra_link_args,
        runtime_library_dirs=runtime_library_dirs,
        define_macros=[("NOMINMAX", None)],
        language="cpp",
    )

    #return [vnctptd, vnctpmd]
    return [vnjeestd]

setup(ext_modules=get_ext_modules())
