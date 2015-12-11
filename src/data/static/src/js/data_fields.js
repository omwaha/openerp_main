openerp.oepetstore = function(instance, local) {
    var _t = instance.web._t,
        _lt = instance.web._lt;
    var QWeb = instance.web.qweb;

    local.HomePage = instance.Widget.extend({
        start: function() {
            console.log("pet store home page loaded");
        },
    });

    instance.web.client_actions.add(
        'petstore.homepage', 'instance.oepetstore.HomePage');
}


local.FieldChar2 = instance.web.form.AbstractField.extend({
    init: function() {
        this._super.apply(this, arguments);
        this.set("value", "");
    },
    start: function() {
        this.on("change:effective_readonly", this, function() {
            this.display_field();
            this.render_value();
        });
        this.display_field();
        return this._super();
    },
    display_field: function() {
        var self = this;
        this.$el.html(QWeb.render("FieldChar2", {widget: this}));
        if (! this.get("effective_readonly")) {
            this.$("input").change(function() {
                self.internal_set_value(self.$("input").val());
            });
        }
    },
    render_value: function() {
        if (this.get("effective_readonly")) {
            this.$el.text(this.get("value"));
        } else {
            this.$("input").val(this.get("value"));
        }
    },
});

instance.web.form.widgets.add('char2', 'instance.oepetstore.FieldChar2');

