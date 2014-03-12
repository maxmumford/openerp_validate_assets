import openerp_rpc_cli

class ValidateAssets(openerp_rpc_cli.openerp_rpc_cli.OpenErpRpcCli):

	description = "Validates all assets that are in draft state"

	def do(self, args, conn):
		assets = conn.get_model('account.asset.asset')
		asset_ids = assets.search([('state', '=', 'draft')])
		assets.validate(asset_ids)
		print "Validated %d assets" % len(asset_ids)

ValidateAssets()
