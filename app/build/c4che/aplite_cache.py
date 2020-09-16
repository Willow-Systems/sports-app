AR = 'arm-none-eabi-ar'
ARFLAGS = 'rcs'
AS = 'arm-none-eabi-gcc'
BINDIR = '/usr/local/bin'
BLOCK_MESSAGE_KEYS = []
BUILD_DIR = 'aplite'
BUILD_TYPE = 'app'
BUNDLE_BIN_DIR = 'aplite'
BUNDLE_NAME = 'app.pbw'
CC = ['arm-none-eabi-gcc']
CCLNK_SRC_F = []
CCLNK_TGT_F = ['-o']
CC_NAME = 'gcc'
CC_SRC_F = []
CC_TGT_F = ['-c', '-o']
CC_VERSION = ('4', '7', '2')
CFLAGS = ['-std=c99', '-mcpu=cortex-m3', '-mthumb', '-ffunction-sections', '-fdata-sections', '-g', '-fPIE', '-Os', '-D_TIME_H_', '-Wall', '-Wextra', '-Werror', '-Wno-unused-parameter', '-Wno-error=unused-function', '-Wno-error=unused-variable']
CFLAGS_MACBUNDLE = ['-fPIC']
CFLAGS_cshlib = ['-fPIC']
CPPPATH_ST = '-I%s'
DEFINES = ['RELEASE', 'PBL_PLATFORM_APLITE', 'PBL_BW', 'PBL_RECT', 'PBL_COMPASS', 'PBL_DISPLAY_WIDTH=144', 'PBL_DISPLAY_HEIGHT=168', 'PBL_SDK_3']
DEFINES_ST = '-D%s'
DEST_BINFMT = 'elf'
DEST_CPU = 'arm'
DEST_OS = 'linux'
INCLUDES = ['aplite']
LD = 'arm-none-eabi-ld'
LIBDIR = '/usr/local/lib'
LIBPATH_ST = '-L%s'
LIB_DIR = 'node_modules'
LIB_JSON = [{u'gitHead': u'946675bdadff2064131a7eeca84b3a2bdd48e7a4', u'_location': u'/pebblejs', u'dist': {u'tarball': u'https://registry.npmjs.org/pebblejs/-/pebblejs-1.0.0.tgz', u'shasum': u'ddf31286fdda533a159a083b9ad2cb2ea8198e8c'}, u'_spec': u'pebblejs', u'_npmOperationalInternal': {u'tmp': u'tmp/pebblejs-1.0.0.tgz_1482176387800_0.8418819417711347', u'host': u'packages-18-east.internal.npmjs.com'}, u'keywords': [u'pebble-package'], u'devDependencies': {u'coffee-script': u'^1.11.1'}, u'_from': u'pebblejs@latest', u'pebble': {u'targetPlatforms': [u'aplite', u'basalt', u'chalk', u'diorite'], u'sdkVersion': u'3', u'projectType': u'package', u'resources': {u'media': [{u'menuIcon': True, u'type': u'bitmap', u'name': u'SIMPLY_IMAGE_MENU_ICON', u'file': u'images/menu_icon.png'}, {u'type': u'bitmap', u'name': u'SIMPLY_IMAGE_LOGO_SPLASH', u'file': u'images/logo_splash.png'}, {u'type': u'bitmap', u'name': u'SIMPLY_IMAGE_TILE_SPLASH', u'file': u'images/tile_splash.png'}, {u'type': u'font', u'name': u'SIMPLY_MONO_FONT_14', u'file': u'fonts/UbuntuMono-Regular.ttf'}]}, u'capabilities': [u'configurable']}, u'_inCache': True, u'_phantomChildren': {}, u'_args': [[u'pebblejs', u'/mnt/e/Pebble Development/pebble-projects/Sports']], u'_nodeVersion': u'7.2.1', u'version': u'1.0.0', u'_resolved': u'https://registry.npmjs.org/pebblejs/-/pebblejs-1.0.0.tgz', u'readme': u'ERROR: No README data found!', u'homepage': u'https://github.com/pebble/pebblejs#readme', u'files': [u'dist.zip'], u'_npmVersion': u'3.10.9', u'_requested': {u'name': u'pebblejs', u'rawSpec': u'', u'raw': u'pebblejs', u'scope': None, u'type': u'tag', u'spec': u'latest'}, u'description': u'Pebble.js =========', u'repository': {u'url': u'git+https://github.com/pebble/pebblejs.git', u'type': u'git'}, u'optionalDependencies': {}, u'_requiredBy': [u'/'], u'maintainers': [{u'name': u'pebble-tech', u'email': u'webteam@getpebble.com'}], u'dependencies': {}, u'scripts': {}, 'path': 'node_modules/pebblejs/dist', u'_installable': True, u'_shrinkwrap': None, u'name': u'pebblejs', u'license': u'MIT', u'directories': {}, u'author': {u'name': u'Meiguro'}, u'bugs': {u'url': u'https://github.com/pebble/pebblejs/issues'}, u'_npmUser': {u'email': u'webteam@getpebble.com', u'name': u'pebble-tech'}, 'js_paths': ['node_modules/pebblejs/dist/js/clock/clock.js', 'node_modules/pebblejs/dist/js/clock/index.js', 'node_modules/pebblejs/dist/js/index.js', 'node_modules/pebblejs/dist/js/lib/ajax.js', 'node_modules/pebblejs/dist/js/lib/color.js', 'node_modules/pebblejs/dist/js/lib/emitter.js', 'node_modules/pebblejs/dist/js/lib/image.js', 'node_modules/pebblejs/dist/js/lib/myutil.js', 'node_modules/pebblejs/dist/js/lib/png-encoder.js', 'node_modules/pebblejs/dist/js/lib/struct.js', 'node_modules/pebblejs/dist/js/lib/util2.js', 'node_modules/pebblejs/dist/js/lib/vector2.js', 'node_modules/pebblejs/dist/js/platform/feature.js', 'node_modules/pebblejs/dist/js/platform/index.js', 'node_modules/pebblejs/dist/js/platform/platform.js', 'node_modules/pebblejs/dist/js/settings/index.js', 'node_modules/pebblejs/dist/js/settings/settings.js', 'node_modules/pebblejs/dist/js/simply/simply.js', 'node_modules/pebblejs/dist/js/smartpackage/package-pebble.js', 'node_modules/pebblejs/dist/js/smartpackage/package.js', 'node_modules/pebblejs/dist/js/timeline/index.js', 'node_modules/pebblejs/dist/js/timeline/timeline.js', 'node_modules/pebblejs/dist/js/ui/accel.js', 'node_modules/pebblejs/dist/js/ui/card.js', 'node_modules/pebblejs/dist/js/ui/circle.js', 'node_modules/pebblejs/dist/js/ui/element.js', 'node_modules/pebblejs/dist/js/ui/image.js', 'node_modules/pebblejs/dist/js/ui/imageservice.js', 'node_modules/pebblejs/dist/js/ui/index.js', 'node_modules/pebblejs/dist/js/ui/inverter.js', 'node_modules/pebblejs/dist/js/ui/light.js', 'node_modules/pebblejs/dist/js/ui/line.js', 'node_modules/pebblejs/dist/js/ui/menu.js', 'node_modules/pebblejs/dist/js/ui/propable.js', 'node_modules/pebblejs/dist/js/ui/radial.js', 'node_modules/pebblejs/dist/js/ui/rect.js', 'node_modules/pebblejs/dist/js/ui/resource.js', 'node_modules/pebblejs/dist/js/ui/simply-pebble.js', 'node_modules/pebblejs/dist/js/ui/simply.js', 'node_modules/pebblejs/dist/js/ui/stage.js', 'node_modules/pebblejs/dist/js/ui/tests.js', 'node_modules/pebblejs/dist/js/ui/text.js', 'node_modules/pebblejs/dist/js/ui/timetext.js', 'node_modules/pebblejs/dist/js/ui/vibe.js', 'node_modules/pebblejs/dist/js/ui/voice.js', 'node_modules/pebblejs/dist/js/ui/window.js', 'node_modules/pebblejs/dist/js/ui/windowstack.js', 'node_modules/pebblejs/dist/js/vendor/moment.js', 'node_modules/pebblejs/dist/js/vendor/png.js', 'node_modules/pebblejs/dist/js/vendor/zlib.js', 'node_modules/pebblejs/dist/js/wakeup/index.js', 'node_modules/pebblejs/dist/js/wakeup/wakeup.js'], u'_where': u'/mnt/e/Pebble Development/pebble-projects/Sports', u'_id': u'pebblejs@1.0.0', u'_shasum': u'ddf31286fdda533a159a083b9ad2cb2ea8198e8c'}]
LIB_RESOURCES_JSON = {u'pebblejs': [{u'menuIcon': True, u'type': u'bitmap', u'name': u'SIMPLY_IMAGE_MENU_ICON', u'file': u'images/menu_icon.png'}, {u'type': u'bitmap', u'name': u'SIMPLY_IMAGE_LOGO_SPLASH', u'file': u'images/logo_splash.png'}, {u'type': u'bitmap', u'name': u'SIMPLY_IMAGE_TILE_SPLASH', u'file': u'images/tile_splash.png'}, {u'type': u'font', u'name': u'SIMPLY_MONO_FONT_14', u'file': u'fonts/UbuntuMono-Regular.ttf'}]}
LIB_ST = '-l%s'
LINKFLAGS = ['-mcpu=cortex-m3', '-mthumb', '-Wl,--gc-sections', '-Wl,--warn-common', '-fPIE', '-Os']
LINKFLAGS_MACBUNDLE = ['-bundle', '-undefined', 'dynamic_lookup']
LINKFLAGS_cshlib = ['-shared']
LINKFLAGS_cstlib = ['-Wl,-Bstatic']
LINK_CC = ['arm-none-eabi-gcc']
MESSAGE_KEYS = {u'dummy': 10000}
MESSAGE_KEYS_DEFINITION = '/mnt/e/Pebble Development/Github Repo/sports-app/app/build/src/message_keys.auto.c'
MESSAGE_KEYS_HEADER = '/mnt/e/Pebble Development/Github Repo/sports-app/app/build/include/message_keys.auto.h'
MESSAGE_KEYS_JSON = '/mnt/e/Pebble Development/Github Repo/sports-app/app/build/js/message_keys.json'
NODE_PATH = '/home/dev/.pebble-sdk/SDKs/current/node_modules'
PEBBLE_SDK_COMMON = '/home/dev/.pebble-sdk/SDKs/current/sdk-core/pebble/common'
PEBBLE_SDK_PLATFORM = '/home/dev/.pebble-sdk/SDKs/current/sdk-core/pebble/aplite'
PEBBLE_SDK_ROOT = '/home/dev/.pebble-sdk/SDKs/current/sdk-core/pebble'
PLATFORM = {'TAGS': ['aplite', 'bw', 'rect', 'compass', '144w', '168h'], 'MAX_FONT_GLYPH_SIZE': 256, 'ADDITIONAL_TEXT_LINES_FOR_PEBBLE_H': [], 'MAX_APP_BINARY_SIZE': 65536, 'MAX_RESOURCES_SIZE': 524288, 'MAX_APP_MEMORY_SIZE': 24576, 'MAX_WORKER_MEMORY_SIZE': 10240, 'NAME': 'aplite', 'BUNDLE_BIN_DIR': 'aplite', 'BUILD_DIR': 'aplite', 'MAX_RESOURCES_SIZE_APPSTORE_2_X': 98304, 'MAX_RESOURCES_SIZE_APPSTORE': 131072, 'DEFINES': ['PBL_PLATFORM_APLITE', 'PBL_BW', 'PBL_RECT', 'PBL_COMPASS', 'PBL_DISPLAY_WIDTH=144', 'PBL_DISPLAY_HEIGHT=168']}
PLATFORM_NAME = 'aplite'
PREFIX = '/usr/local'
PROJECT_INFO = {'appKeys': {u'dummy': 10000}, u'watchapp': {u'watchface': False}, u'displayName': u'Sports', u'uuid': u'9e57a249-9a5c-4ded-b374-005a472b8049', u'messageKeys': {u'dummy': 10000}, 'companyName': u'itsthered1', u'enableMultiJS': True, u'sdkVersion': u'3', 'versionLabel': u'0.0', u'targetPlatforms': [u'aplite', u'basalt', u'chalk', u'diorite'], 'longName': u'Sports', 'shortName': u'Sports', u'resources': {u'media': [{u'type': u'png', u'name': u'hockey_puck', u'file': u'hockey_puck.png'}, {u'type': u'png', u'name': u'soccer_ball', u'file': u'soccer_ball.png'}, {u'type': u'png', u'name': u'basketball', u'file': u'basketball.png'}, {u'type': u'png', u'name': u'baseball', u'file': u'baseball.png'}, {u'type': u'png', u'name': u'american_football', u'file': u'american_football.png'}]}, 'name': u'Sports'}
REQUESTED_PLATFORMS = [u'aplite', u'basalt', u'chalk', u'diorite']
RESOURCES_JSON = [{u'type': u'png', u'name': u'hockey_puck', u'file': u'hockey_puck.png'}, {u'type': u'png', u'name': u'soccer_ball', u'file': u'soccer_ball.png'}, {u'type': u'png', u'name': u'basketball', u'file': u'basketball.png'}, {u'type': u'png', u'name': u'baseball', u'file': u'baseball.png'}, {u'type': u'png', u'name': u'american_football', u'file': u'american_football.png'}]
RPATH_ST = '-Wl,-rpath,%s'
SANDBOX = False
SDK_VERSION_MAJOR = 5
SDK_VERSION_MINOR = 78
SHLIB_MARKER = None
SIZE = 'arm-none-eabi-size'
SONAME_ST = '-Wl,-h,%s'
STLIBPATH_ST = '-L%s'
STLIB_MARKER = None
STLIB_ST = '-l%s'
SUPPORTED_PLATFORMS = ['aplite', 'basalt', 'chalk', 'diorite', 'emery']
TARGET_PLATFORMS = ['diorite', 'chalk', 'basalt', 'aplite']
TIMESTAMP = 1600276643
USE_GROUPS = True
VERBOSE = 0
WEBPACK = '/home/dev/.pebble-sdk/SDKs/current/node_modules/.bin/webpack'
cprogram_PATTERN = '%s'
cshlib_PATTERN = 'lib%s.so'
cstlib_PATTERN = 'lib%s.a'
macbundle_PATTERN = '%s.bundle'
